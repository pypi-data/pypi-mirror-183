from .classes import CompoundMapper, HGNCMapper, EnsemblMapper, MyGeneMapper

idm = CompoundMapper([EnsemblMapper(list_all_hits=True),HGNCMapper(list_all_hits=True),MyGeneMapper()])

