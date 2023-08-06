from biothings_client import get_client
from pathlib import Path
from .utils import *


class Source:
	def __init__(self, source_id, list_all_hits=False, fill_value='N/A'):
		self.source_id = source_id

		self._list_all_hits = list_all_hits  # whether to list all possible gene conversion hits when there are multiple options (one-to-many)

		self._fill_value = fill_value

	def sanitize(self, id_list, id_in, id_out):
		if not self.has_id_in_type(id_in):
			raise ValueError(f'{self.source_id}: invalid input ID type')
		if not self.has_id_out_type(id_out):
			raise ValueError(f'{self.source_id}: invalid output ID type')

		return list(map(str, make_list(id_list)))


class LocalSource(Source):
	def __init__(self, source_id, data, list_all_hits=False, selection_func_dict=None, fill_value='N/A'):
		super().__init__(source_id, list_all_hits=list_all_hits, fill_value=fill_value)

		if selection_func_dict is None:
			selection_func_dict = {}

		self._selection_func_dict = \
			{'entr': lambda id_in, id_out_list: min(map(int, id_out_list)),
			 'symb': lambda id_in, id_out_list: min(id_out_list, key=len),
			 'ensg': lambda id_in, id_out_list: min(id_out_list)}
		self._selection_func_dict.update(selection_func_dict)

		self._data = data
		self.init()

	def init(self):
		data = self._data
		self._lookup = {}

		id_types = data.columns.tolist()
		for id_in in id_types:
			self._lookup[id_in] = {}
			for id_out in id_types:
				if id_in == id_out:
					continue
				if self._list_all_hits:
					self._lookup[id_in][id_out] = self.gen_lookup_table(data, id_in, id_out,
																		lambda id_in, id_out_list: '|'.join(
																			id_out_list))
				else:
					self._lookup[id_in][id_out] = self.gen_lookup_table(data, id_in, id_out,
																		self._selection_func_dict[id_out])

	def convert(self, id_list, id_in, id_out):
		id_list = self.sanitize(id_list, id_in, id_out)
		return self._lookup[id_in][id_out].reindex(id_list, fill_value=self._fill_value)

	def gen_lookup_table(self, data, id_in, id_out, selection_func):
		pruned = data[data[id_in].notna() & data[id_out].notna()]
		pruned = pruned[~pruned.duplicated(subset=[id_in, id_out])]
		id_in_unq = ~pruned.duplicated(subset=[id_in], keep=False)
		unq = pruned.loc[id_in_unq].set_index(id_in)[id_out]

		if (~id_in_unq).sum() > 0:
			nonunq = pruned.loc[~id_in_unq, [id_in, id_out]].groupby(id_in).apply(
				lambda x: selection_func(x.name, x[id_out]))
			# nonunq = pruned.loc[~id_in_unq, [id_in, id_out]].groupby(id_in).apply(lambda x: print(x))
			lookup = pd.concat([unq, nonunq])
		else:
			lookup = unq
		return lookup

	def integrate_synonyms(self, data, id_orig, id_synonym):
		pruned = data[data[id_orig].notna() & data[id_synonym].notna()]
		pruned = pruned[~pruned.duplicated(subset=[id_orig, id_synonym])]
		pruned = pruned[~pruned.duplicated(subset=[id_synonym], keep=False)]  # we just remove inconsistent synonyms
		for id_out in self._lookup[id_orig].keys():
			lookup = self._lookup[id_orig][id_out]
			pruned_curr = pruned.loc[~pruned[id_synonym].isin(lookup.index) & pruned[id_orig].isin(lookup.index)].copy()
			pruned_curr[id_out] = lookup.loc[pruned_curr[id_orig].values].values
			if pruned_curr.shape[0] > 0:
				pruned_curr = pruned_curr.set_index(id_synonym)[id_out].squeeze()
				self._lookup[id_orig][id_out] = pd.concat([lookup, pruned_curr])

	def has_id_in_type(self, id_type):
		return id_type in self._data.columns

	def has_id_out_type(self, id_type):
		return id_type in self._data.columns

	def lookup_size(self):
		for id_in, id_in_dict in self._lookup.items():
			for id_out, id_out_dict in id_in_dict.items():
				print(id_in, ' ->', id_out, ':', len(id_out_dict))


class EnsemblBiomart(LocalSource):
	def __init__(self, data_path=None, list_all_hits=False, selection_func_dict=None, symb_aliases=True,
				 fill_value='N/A'):
		if selection_func_dict is None:
			selection_func_dict = {}
		if data_path is None:
			data_path = Path('data/ensembl.tsv')
			if not data_path.exists():
				print('- Biomart data has not been downloaded yet, downloading...')
				download_ensembl(str(data_path))
		data = pd.read_table(data_path, sep='\t', dtype={'entr': 'str'})
		main_data = data[['ensg', 'entr', 'symb']]
		syn_data = data[['symb', 'synonym']]
		super().__init__(source_id='ensembl', data=main_data, list_all_hits=list_all_hits, selection_func_dict=selection_func_dict, fill_value=fill_value)
		if symb_aliases:
			self.integrate_synonyms(syn_data, 'symb', 'synonym')


class HGNCBiomart(LocalSource):
	def __init__(self, data_path=None, list_all_hits=False, selection_func_dict=None, symb_aliases=True,
				 fill_value='N/A'):
		if selection_func_dict is None:
			selection_func_dict = []
		if data_path is None:
			data_path = Path('data/hgnc.tsv')
			if not data_path.exists():
				print('- Biomart data has not been downloaded yet, downloading...')
				download_hgnc(str(data_path))
		data = pd.read_table(data_path, sep='\t', dtype={'entr': 'str'})
		main_data = data[['ensg', 'entr', 'symb']]
		syn_data = data[['symb', 'synonym1', 'synonym2']]
		super().__init__(source_id='hgnc', data=main_data, list_all_hits=list_all_hits, selection_func_dict=selection_func_dict, fill_value=fill_value)
		if symb_aliases:
			self.integrate_synonyms(syn_data, 'symb', 'synonym1')
			self.integrate_synonyms(syn_data, 'symb', 'synonym2')


class RemoteSource(Source):
	def __init__(self, source_id, list_all_hits=False, fill_value='N/A'):
		super().__init__(source_id, list_all_hits=list_all_hits, fill_value=fill_value)


class MyGene(RemoteSource):
	mg = get_client('gene')

	def __init__(self, list_all_hits=False, fill_value='N/A'):
		super().__init__('mygene', list_all_hits=False, fill_value=fill_value)

	def convert(self, id_list, id_in, id_out):
		id_list = self.sanitize(id_list, id_in, id_out)

		id_relabel = {'entr': 'entrezgene', 'symb': 'symbol', 'ensg': 'ensembl.gene'}
		output = MyGene.mg.getgenes(id_list, scopes=id_relabel[id_in], fields=id_relabel[id_out],
									species='human', as_dataframe=True, returnall=True)

		return output[id_relabel[id_out]].fillna(self._fill_value)

	def has_id_in_type(self, id_type):
		return id_type in ['entr', 'ensg']

	def has_id_out_type(self, id_type):
		return id_type in ['entr', 'ensg', 'symb']


class IDMapper:
	def __init__(self, sources):
		self._sources = make_list(sources)
		self._src_ids = [src.source_id for src in self._sources]
		self._fill_value = self._sources[0]._fill_value

	def get_source(self, source_id):
		return self._sources[self._src_ids.index(source_id)]

	def convert(self, id_list, id_in, id_out, report=False):
		id_list = make_list(id_list)
		src_ids = [src_id for src_id, src in zip(self._src_ids, self._sources) if src.has_id_in_type(id_in) and src.has_id_out_type(id_out)]
		if len(src_ids) == 0:
			raise ValueError('Input or output ID type not supported by selected sources')
		out_df = pd.DataFrame([], columns=[src_ids])
		for src_id in src_ids:
			out_df[src_id] = self.get_source(src_id).convert(id_list, id_in, id_out)

		id_list_out = out_df[src_ids[0]].squeeze(axis=1)
		for i in range(1, len(src_ids)):
			idx = id_list_out == self._fill_value
			if idx.sum().squeeze() == 0:
				break
			id_list_out[idx] = out_df.loc[idx, src_ids[i]].squeeze(axis=1)

		if report:
			report_df = pd.concat([out_df[src_id] for src_id in src_ids], axis=1)
			if any([src._list_all_hits for src in self._sources]):
				report_df['Mismatch'] = report_df.apply(lambda x: no_intersection(x[x != self._fill_value].values),
														axis=1)
			else:
				report_df['Mismatch'] = report_df.apply(lambda x: x[x != self._fill_value].nunique() > 1, axis=1)
			return id_list_out.values.tolist(), report_df
		if is_list(id_list):
			return id_list_out.values.tolist()
		else:
			return id_list_out.values.tolist()[0]

	def entr2ensg(self, id_list, report=False):
		return self.convert(id_list, id_in='entr', id_out='ensg', report=report)

	def entr2symb(self, id_list, report=False):
		return self.convert(id_list, id_in='entr', id_out='symb', report=report)

	def ensg2entr(self, id_list, report=False):
		return self.convert(id_list, id_in='ensg', id_out='entr', report=report)

	def ensg2symb(self, id_list, report=False):
		return self.convert(id_list, id_in='ensg', id_out='symb', report=report)

	def symb2entr(self, id_list, report=False):
		return self.convert(id_list, id_in='symb', id_out='entr', report=report)

	def symb2ensg(self, id_list, report=False):
		return self.convert(id_list, id_in='symb', id_out='ensg', report=report)
