import sharppy.io.decoder as decoder
import sharppy.io.buf_decoder as buf_decoder
import sharppy.io.spc_decoder as spc_decoder
import sharppy.io.pecan_decoder as pecan_decoder
"""
    Unit tests to test to see if decoders work on different file types
"""
files = ['examples/data/14061619.OAX',
         'examples/data/rap_oun.buf',
         'examples/data/ABR.txt',
         'examples/data/OUN.txt']
   
def test_decoder():
   
    decoders = decoder.getDecoders()
    assert len(decoders) > 0
    
    dec = spc_decoder.SPCDecoder(files[0])
    dec = buf_decoder.BufDecoder(files[1])
    profs = dec.getProfiles()
    stn_id = dec.getStnId()

    assert profs.isEnsemble() == False
    assert profs.isInterpolated() == False
    assert profs.isModified() == False
    assert profs.getAnalogDate() is None
    assert profs.hasCurrentProf() == True
    
    #profs.interp()
    #profs.resetInterpolation()
    #dec = pecan_decoder.PECANDecoder(files[2])
    #dec = pecan_decoder.PECANDecoder(files[3])

    print(profs) 
test_decoder()
