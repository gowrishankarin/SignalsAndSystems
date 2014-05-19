#Parameters
#
# - Fs		: Sampling Frequency
# - F0		: Frequency of the notes forming chrod
# - Gains	: Gains of individual notes in the chord
# - Duration: Duration of the chord in second
# - Alpha	: Attenuation in KS algorithm
Fs = 48000
class KarplusStrongA4:
    
    def ks_wave(self, x, alpha, D):
        import numpy as np
        from KarplusStrong import KarplusStrong
        ks = KarplusStrong()
        F0 = 440*np.array([pow(2, (-31./12.)), pow(2, (-19./12.)), pow(2, (-16./12.)), 
                           pow(2, (-14./12.)), pow(2, (-4./12.)), pow(2, (3./12.)), 
                            pow(2, (10./12.))])
                            
        gain = np.array([1.2, 3.0, 1.0, 2.2, 1.0, 1.0, 3.5])
        
        duration = 4
        alpha = 0.9785
        
        noSampleInChord = Fs*duration
        
        
        firstDuration = np.ceil(float(noSampleInChord)/round(float(Fs)/float(F0[0])))
        
        chord = np.zeros(noSampleInChord)
        
        for i in range(len(F0)):
            
            currentM = round(float(Fs)/float(F0[i]))
            currentDuration = np.ceil(float(noSampleInChord)/float(currentM))
            
            currentAlpha = pow(alpha, (float(firstDuration)/float(currentM)))
            
            if i == 2:
                currentAlpha = pow(currentAlpha, 8)
                
            x = np.random.rand(currentM)
            y = ks.ks_loop(x, currentAlpha, currentDuration)
            y = y[0:noSampleInChord]
            
            chord = chord + gain[i] * y
        return chord
            
    def write_wave(chord):
        import numpy as np
        from scipy.io.wavfile import write
        
        data = chord
        scaled = np.int16(data/np.max(np.abs(data)) * 32767)
        
        write('hard-days.wav', 44100, scaled)