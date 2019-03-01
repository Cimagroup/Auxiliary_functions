import numpy as np

def persistent_entropy(dgm,dim, inf = False, valInf = np.float(0.0)):
    # From a diagram generated using ripser, this function computes its persistent 
    # entropy. If inf = True, this mean that we want to keep infinity bars. Therefore,
    # it is important to give a value to the infinity valInf. To keep stability,
    # the value must be the same for all persistence diagram we are comparing.
    if inf == False:
        dgm = dgm[dim][dgm[dim][:,1]<np.inf]
        l = dgm[:,1]-dgm[:,0]
        L = np.sum(l)
        p = l/L
        E = -np.sum(p*np.log(p))
    else:
        dgm_valInf = dgm
        dgm_valInf[dim][dgm_valInf[dim][:,1]==np.inf]=np.array([0,valInf])
        l = dgm_valInf[dim][:,1]-dgm_valInf[dim][:,0]
        L = np.sum(l)
        p = l/L
        E = -np.sum(p*np.log(p))
    return E
