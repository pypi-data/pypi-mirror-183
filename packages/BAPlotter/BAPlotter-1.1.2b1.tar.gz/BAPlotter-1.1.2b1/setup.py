from setuptools import setup, find_packages

# 1.2.0.dev1  # Development release
# 1.2.0a1     # Alpha Release
# 1.2.0b1     # Beta Release
# 1.2.0rc1    # Release Candidate
# 1.2.0       # Final Release
# 1.2.0.post1 # Post Release
# 15.10       # Date based release
# 23          # Serial release

setup(
    name='BAPlotter',
    description = 'Plotting of band gap alignments for a list of materials. The user can specify the material names, valence band maximum energies, and conduction band minimum energies. The resulting plot includes a gradient representation of the valence band minimum and conduction band maximum for each material',
    version='1.1.2b1',
    license='MIT',
    author="Sara A. Tolba",
    author_email='sarahtolba1@gmail.com',
    python_requires='>=3',
    packages=find_packages(''),
    package_dir={'': 'src'},
    url='https://github.com/SaraTolba/BandAligmentPlotter',
    keywords='band gap alignment plotter,conduction band,valence band,fermi level',
    install_requires=[
          'matplotlib',
      ],

)