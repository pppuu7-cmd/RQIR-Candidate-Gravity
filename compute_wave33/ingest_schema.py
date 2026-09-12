import numpy as np
from common import COORDS,XSTAR,surrogate_matrix,write

def valid(obj):
    try:
        if obj.get('coordinates')!=COORDS: return False
        if obj.get('closure') is None or obj.get('source') is None: return False
        M=np.asarray(obj['stability_matrix'],float)
        x=np.asarray(obj['fixed_point'],float)
        return M.shape==(5,5) and x.shape==(5,) and np.all(np.isfinite(M)) and np.all(np.isfinite(x))
    except Exception:
        return False

base={'coordinates':COORDS,'fixed_point':XSTAR.tolist(),'stability_matrix':surrogate_matrix().tolist(),'closure':'controlled-surrogate-test','source':'F1 Truncation-4 published spectrum; synthetic canonical orientation'}
accepted=valid(base)
wrong_shape=dict(base); wrong_shape['stability_matrix']=[[1,2],[3,4]]
wrong_coords=dict(base); wrong_coords['coordinates']=['a']*5
missing_meta=dict(base); missing_meta.pop('closure')
nonfinite=dict(base); nonfinite['stability_matrix']=surrogate_matrix().tolist(); nonfinite['stability_matrix'][0][0]=float('nan')
signals={
 'valid_5x5_orientation_object_accepted':accepted,
 'wrong_shape_rejected':not valid(wrong_shape),
 'coordinate_mismatch_rejected':not valid(wrong_coords),
 'incomplete_metadata_rejected':not valid(missing_meta),
 'nonfinite_matrix_rejected':not valid(nonfinite)
}
out={'test':'ingest_schema','signals':signals}; write('wave33_ingest_schema.json',out); assert all(signals.values())
