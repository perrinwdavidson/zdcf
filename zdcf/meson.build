project('zdcf', 'fortran',
  version: '0.1.0',
  meson_version: '>=0.64.0',
  default_options: ['warning_level=1'],
)

py = import('python').find_installation(pure: false)

# Where platform-specific Python modules/extensions should be installed
py_platlib = py.get_install_dir()

# Fortran + f2py interface sources
sources = files('src/zdcf/_fortran/zdcf.pyf', 'src/zdcf/_fortran/zdcf.f')
modname = '_zdcf'

# Extension suffix, e.g. ".cpython-312-darwin.so"
ext = run_command(
  py, '-c',
  'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX") or "")',
  check: true
).stdout().strip()

# Build the f2py extension
zdcf_mod = custom_target(
  'zdcf_extension',
  input: sources,
  output: modname + ext,
  command: [
    py.full_path(), '-m', 'numpy.f2py',
    '-c', '@INPUT0@', '@INPUT1@',
    '-m', modname,
  ],
  build_by_default: true,
  install: true,
  # IMPORTANT: install into platlib via Meson’s python installation mapping
  install_dir: join_paths(py_platlib, 'zdcf'),
)

# Install the pure-Python package directory (src/ layout)
install_subdir(
  'src/zdcf',
  install_dir: join_paths(py_platlib, 'zdcf'),
  strip_directory: true,
)