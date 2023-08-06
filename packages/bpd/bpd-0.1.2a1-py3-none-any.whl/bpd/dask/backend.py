from bpd import _DASK_, _DASK_ENDPOINT_, _DEFAULT_BACKEND_
import os
client = None
if _DEFAULT_BACKEND_ == _DASK_:
    from distributed import Client
    try: 
        client = Client(os.environ["DASK_ENDPOINT"])
    except:
        client = Client(_DASK_ENDPOINT_)
