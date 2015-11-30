import cambex

camb = cambex.CambSession()
camb.set_base_params('/u/mhasse/code/camb/camb_nov15/params2.ini')
cout = camb.run()
print cout.stdout

scal = camb.load_scalarCls()
print scal.EE

camb.set_transfer_redshifts([0., 0.1, 0.2])
cout = camb.run()
print cout.stdout

powerspec, transferfunc = camb.load_transfers()
i = powerspec.P.argmax()
print powerspec.k[i], powerspec.P[1, i]
