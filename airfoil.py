def naca4_symmetric ( t, c, x ):

#*****************************************************************************80
#
## NACA4_SYMMETRIC evaluates y(x) for a NACA symmetric 4-digit airfoil.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eastman Jacobs, Kenneth Ward, Robert Pinkerton,
#    "The characteristics of 78 related airfoil sections from tests in
#    the variable-density wind tunnel",
#    NACA Report 460, 1933.
#
#  Parameters:
#
#    Input, real T, the maximum relative thickness.
#
#    Input, real C, the chord length.
#
#    Input, real X(*), points along the chord length.  
#    0.0 <= X(*) <= C.
#
#    Output, real Y(*), for each value of X, the corresponding value of Y
#    so that (X,Y) is on the upper wing surface, and (X,-Y) is on the
#    lower wing surface.
#
  import numpy as np

  y = 5.0 * t * c * ( \
    0.2969 * np.sqrt ( x / c )\
    + (((( \
      - 0.1015 ) * ( x / c ) \
      + 0.2843 ) * ( x / c ) \
      - 0.3516 ) * ( x / c ) \
      - 0.1260 ) * ( x / c ) )

  return y

def naca4_symmetric_test ( ):

#*****************************************************************************80
#
## NACA4_SYMMETRIC_TEST tests NACA4_SYMMETRIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'NACA4_SYMMETRIC_TEST' )
  print ( '  NACA4_SYMMETRIC evaluates y(x) for a NACA' )
  print ( '  symmetric airfoil defined by a 4-digit code.' )

  c = 500.0
  t = 0.25
  n = 51
  x = np.linspace ( 0.0, c, n )
  x2 = np.append ( x, np.flip ( x, 0 ) )
  y = naca4_symmetric ( t, c, x )
  y2 = np.append ( y, np.flip ( -y, 0 ) )
#
#  Plot the wing surface.
#
  plt.plot ( x2, y2, 'b-', linewidth = 3 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.xlabel ( '<---X--->', fontsize = 16 )
  plt.ylabel ( '<---Y--->', fontsize = 16 )
  plt.title ( 'NACA 4-digit symmetric airfoil', fontsize = 24 )

  filename = 'naca4_symmetric_test.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved in file "%s"' % ( filename ) )
  plt.show ( )
#
#  Save data to a file.
#
  filename = 'naca4_symmetric_test.txt'
  output = open ( filename, 'w' )
  for i in range ( 0, 2 * n ):
    s = '  %g  %g\n' % ( x2[i], y2[i] )
    output.write ( s )
  output.close ( )
  print ( '  Data saved in file "%s"' % ( filename ) )

  return

if ( __name__ == '__main__' ):
  naca4_symmetric_test ( )
