from __future__ import print_function

import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import c_ast, parse_file


# A simple visitor for FuncDef nodes that prints the names and
# locations of function definitions.
class FuncDefVisitor(c_ast.NodeVisitor):
	def visit_FuncDef(self, node):
		print('%s at %s' % (node.decl.name, node.decl.coord))


def show_func_defs(filename):
	# Note that cpp is used. Provide a path to your own cpp or
	# make sure one exists in PATH.
	print(filename)
	ast = parse_file(filename,
	                 use_cpp=True,
	                 cpp_path='gcc',
	                 cpp_args=[#r'-x', r'objective-c++',
	                            #r'-std=c++11',
	                            #r'-mmacosx-version-min=10.13',
	                            #r'-framework', r'Metal',
	                            #r'-framework', r'MetalKit',
	                            #r'-framework', r'Cocoa',
	                            #r'-framework', r'CoreFoundation',
	                            #r'-fobjc-link-runtime'
	                 ])

	v = FuncDefVisitor()
	v.visit(ast)


if __name__ == "__main__":
	work_dir = "/".join(__file__.split("/")[:-2])

	filename = str(work_dir + '/mtlpp/examples/00_init.cpp').replace(" ", "\ ")

	show_func_defs(filename)
