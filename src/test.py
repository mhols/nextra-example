import nextra as nx
import sys
import os
import settings_narval_vega2018
import matplotlib.pyplot as plt


N = nx.Night(os.path.join(__file__, '../../../nextra-data/Vega_narval_test/'), **settings_narval_vega2018.get_kwargs())

N.set_id('STELLAR_11_4_V')

nx.store.rm(os.path.abspath(__file__+'../../../../nextra-data/Vega_narval_test/276762o.fits'))
nx.store.rm(os.path.abspath(__file__+'../../../../nextra-data/Vega_narval_test/276748c.fits'))

order = 60 
s = N.star4[0]

plt.figure()
plt.title(f'bare_voie1 {s.fitsfile}')
plt.plot(s.bare_voie1[order])
plt.ylim(0, 280000)

plt.figure()
plt.title(f'voie1 {s.fitsfile}')
plt.plot(s.voie1[order])
plt.plot(s.voie1[order]*s.Il[order])

plt.figure()
plt.title(f'beam_sum_blaze {s.fitsfile}')
plt.plot( s.beams[order].beam_sum_blaze(s.masterflat))

plt.figure()
plt.title(f'_xx, _yy {s.fitsfile}')
plt.plot(s.beams[order]._xx, s.beams[order]._yy, '.')
plt.plot(s.beams[order]._xx, s.beams[order](s.beams[order]._xx))


plt.show()



I = N.stokes.true_order_number==order
lam, intens = N.stokes.lambdagrid[I], N.stokes.intensity[I]

plt.figure()
plt.plot( lam, intens / intens.max())

plt.show()