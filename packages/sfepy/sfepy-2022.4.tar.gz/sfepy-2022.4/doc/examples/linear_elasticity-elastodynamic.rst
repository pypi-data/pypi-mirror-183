.. _linear_elasticity-elastodynamic:

linear_elasticity/elastodynamic.py
==================================

**Description**


The linear elastodynamics solution of an iron plate impact problem.

Find :math:`\ul{u}` such that:

.. math::
    \int_{\Omega} \rho \ul{v} \pddiff{\ul{u}}{t}
    + \int_{\Omega} D_{ijkl}\ e_{ij}(\ul{v}) e_{kl}(\ul{u})
    = 0
    \;, \quad \forall \ul{v} \;,

where

.. math::
    D_{ijkl} = \mu (\delta_{ik} \delta_{jl}+\delta_{il} \delta_{jk}) +
    \lambda \ \delta_{ij} \delta_{kl}
    \;.

Notes
-----

The used elastodynamics solvers expect that the total vector of DOFs contains
three blocks in this order: the displacements, the velocities, and the
accelerations. This is achieved by defining three unknown variables ``'u'``,
``'du'``, ``'ddu'`` and the corresponding test variables, see the `variables`
definition. Then the solver can automatically extract the mass, damping (zero
here), and stiffness matrices as diagonal blocks of the global matrix. Note
also the use of the ``'dw_zero'`` (do-nothing) term that prevents the
velocity-related variables to be removed from the equations in the absence of a
damping term.

Usage Examples
--------------

Run with the default settings (the Newmark method, 3D problem, results stored
in ``output/ed/``)::

  sfepy-run sfepy/examples/linear_elasticity/elastodynamic.py

Solve using the Bathe method::

  sfepy-run sfepy/examples/linear_elasticity/elastodynamic.py -O "ts='tsb'"

View the resulting displacements on the deforming mesh (1000x magnified),
Cauchy strain and stress using::

  sfepy-view output/ed/user_block.h5 -f u:wu:f1e3:p0 1:vw:p0 cauchy_strain:p1 cauchy_stress:p2

Solve in 2D using the explicit Velocity-Verlet method with adaptive
time-stepping and save all time steps (see ``plot_times.py`` use below)::

  sfepy-run sfepy/examples/linear_elasticity/elastodynamic.py -d "dims=(5e-3, 5e-3), shape=(61, 61), tss_name='tsvv', adaptive=True, save_times='all'"

View the resulting velocities on the deforming mesh (1000x magnified) using::

  sfepy-view output/ed/user_block.h5 -2 --grid-vector1=1.2,0,0 -f du:wu:f1e3:p0 1:vw:p0

Plot the adaptive time steps (available at times according to 'save_times'
option!)::

  python3 sfepy/scripts/plot_times.py output/ed/user_block.h5 -l

Again, solve in 2D using the explicit Velocity-Verlet method with adaptive
time-stepping and save all time steps. Now the used time step control is
suitable for linear problems solved by a direct solver: it employs a heuristic
that tries to keep the time step size constant for several consecutive steps,
reducing so the need for a new matrix factorization. Run::

  sfepy-run sfepy/examples/linear_elasticity/elastodynamic.py -d "dims=(5e-3, 5e-3), shape=(61, 61), tss_name='tsvv', tsc_name='tscedl', adaptive=True, save_times='all'"

The resulting velocities and adaptive time steps can again be plotted by the
commands shown above.


.. image:: /../doc/images/gallery/linear_elasticity-elastodynamic.png


:download:`source code </../sfepy/examples/linear_elasticity/elastodynamic.py>`

.. literalinclude:: /../sfepy/examples/linear_elasticity/elastodynamic.py

