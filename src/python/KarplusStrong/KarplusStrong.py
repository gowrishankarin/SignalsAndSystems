class KarplusStrong:
    def ks_loop(self, x, alpha, D):
        import numpy as np
        
        if D < 1:
            print('Duration D must be greater than 1')
            
        if x.ndim != 1:
            print('The array entered is of the wrong size')
            return None
            
        M = len(x)
        
        size_y = D*M
        
        y = np.zeros((size_y, 1))
        
        for i in range(M):
            y[i] = x[i]
            
        for index in range(M+1, size_y):
            y[index] = float(alpha*y[index - M])
            
        return y
	
    def ks_mat(self, x, alpha, D):
	import numpy as np

	if D < 1:
		print('Duration D must be greater than 1')
	
	if x.ndim != 1:
		print('The array entered is of the wrong size')
		return None

	M = len(x)
	
	a = np.ones((1,D)) * alpha
	b = np.arange(D)
	alphaVector = pow(a, b)
	
	alphaMatrix = np.eye(D, M)
	for index in range(M):
		alphaMatrix[:, index] = alphaVector

	xMatrix = np.tile(x, (D, 1))
	
	yMatrix = alphaMatrix * xMatrix

	yMatrix.flatten()
	
	return yMatrix