# cambex
Python wrapper for calling CAMB executable and retrieving results.

Building and installing
-----------------------

You can use the Makefile to "make install".  If you want to install to some
local prefix instead of the system default, you can create a file called
Makefile.local and set it to say, for example:


  PREFIX = /home/myname/build/

You will also need to tell cambex where your CAMB binary is.  Do this at the
top of python/base.py, prior to installing, or simply pass camb_bin when you
instantiate a CambSession.


Using
-----

The interface will change in future versions so don't carve your code into any
stones.

```python
import cambex

camb = cambex.CambSession(camb_bin='/u/mhasse/code/camb/camb_nov15/camb')
camb.set_base_params('/u/mhasse/code/camb/camb_nov15/params2.ini')
cout = camb.run()
print cout.stdout

scal = camb.load_scalarCls()
print scal.ell, scal.EE

# And with matter power spectrum
camb.set_transfer_redshifts([0., 0.1, 0.2])
cout = camb.run()

powerspec, transferfunc = camb.load_transfers()

# ... is peaking at
for redshift_i, redshift in enumerate(camb.redshifts):
    i = powerspec.P[redshift_i].argmax()
    print redshift, powerspec.k[i], powerspec.P[redshift_i, i]
```
