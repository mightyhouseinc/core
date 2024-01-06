from sys import argv
from os.path import isfile
from shutil import copy2

# Validate arguments
if len(argv) != 2:
	print('Invalid number of arguments, you should pass the location of \'node.gyp\'.')
	print('Usage: python3 NodeJSGYPPatch.py <path_to_node_gyp>')
	exit(1)

# Validate the project file
if not isfile(argv[1]) or not argv[1].endswith('node.gyp'):
	print('The file \'' + argv[1] + '\' does not exist or is not a valid gyp file, it must be named as \'node.gyp\'.')
	exit(2)

with open(argv[1]) as f:
	nodegyp = eval(f.read())
# Validate that the target is present and it is correct
target = next((x for x in nodegyp['targets'] if 'target_name' in x and x['target_name'] == '<(node_lib_target_name)'), None)

if target is None:
	print('Invalid node.gyp configuration, the target \'node_lib_target_name\' is not present.')
	exit(3)

condition = next((x for x in target['conditions'] if x[0] == 'OS=="win"'), None)

if condition is None or len(condition) != 2:
	print('Invalid node.gyp configuration, the condition \'OS=="win"\' is not present in target \'node_lib_target_name\'.')
	exit(4)

if 'libraries' not in condition[1]:
	print('Invalid node.gyp configuration, \'libraries\' field is not present in the condition \'OS=="win"\' of the target target \'node_lib_target_name\'.')
	exit(5)

# Get the libraries
libraries = condition[1]['libraries']

# Check if the library to patch is present
if 'Winmm' not in libraries:
	# Copy file as backup
	copy2(argv[1], f'{argv[1]}.backup')

	# Apply the patch to the libraries
	libraries.append('Winmm')

	with open(argv[1], 'w') as f:
		f.write(repr(nodegyp))
print('Build project node.gyp patched correctly')
