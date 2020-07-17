from hdr_parser import *
import re

def normalize_class_name(name):
    return re.sub(r"^cv\.", "", name).replace(".", "_")

def normalize_const_name(name):
    return re.sub(r"^const cv\.", "", name).replace(".", "_")

parser = CppHeaderParser(generate_umat_decls=False, generate_gpumat_decls=False)
allowed_func_list = []

with open("funclist.csv", "r") as f:
    allowed_func_list = f.readlines()
    allowed_func_list = [x[:-1] for x in allowed_func_list]
decls = []
for hname in opencv_hdr_list:
    decls += parser.parse(hname)

modlist = []
classlist = []

argtypes = []
defvals = []
def print_arg_function(arg):
    print(","+normalize_class_name(arg[1]), end="")
    argtypes.append(arg[0])
    defvals.append(arg[0]+":"+arg[2])
    # print("\tTYPE:",arg[0], " NAME: ", normalize_class_name(arg[1]), " DEFAULT VALUE: ", arg[2], " MODS: ", arg[3])
    modlist.extend(arg[3])

def print_arg_enum(arg):
    # print("\tNAME:",normalize_const_name(arg[0]), " POS: ", arg[1], " DEFAULT VALUE: ", arg[2], " MODS: ", arg[3])
    modlist.extend(arg[3])

for decl in decls:
    c1 = decl[0].split(' ')
    s = ""
    if len(c1)!=1 and c1[0].startswith("enum"):
        # print("TYPE: ", c1[0], " NAME: ", normalize_class_name(c1[1]))
        if decl[1]!='':
            assert(0)
            # print(decl[1])
        if len(decl[2]) != 0:
            assert(0)
        # for var in decl[3]:
        #     print_arg_enum(var)
    elif len(c1)==1:
        parts = c1[0].split('.')
        if 'mix' in c1[0]:
            # print(decl)
            pass
            # input()
        try:
            if c1[0] not in allowed_func_list:
                pass
            print(c1[0]+","+ decl[1], end="")
            modlist.extend(decl[2])
            for var in decl[3]:
                print_arg_function(var)
            print("")
        except Exception as identifier:
            print(identifier)
            pass
        # if decl[4]!=decl[1]:
        #     print("Modifited Return: ", decl[4])
            # input()
            # assert(0)
    elif len(c1)!=1 and c1[0].startswith("class"):
        pass
        # print("TYPE: ", c1[0], " NAME: ", normalize_class_name(c1[1]), "modlist = ", decl[2])
        # classlist.append(normalize_class_name(c1[1]))
        # modlist.extend(decl[2])
        # if decl[1]!='':
        #     print(decl[1])
        # for var in decl[3]:
        #     print_arg_enum(var)
    else:
        print(decl)
# decl = decls[0]tor_Point2f', 'vector_Mat', 'double', 'Rect*', 'c_string', 'Moments', 'String', 'vector_Rect2d', 'TermCriteria', 'vector_RotatedRect', 'vector_Rect', 'RNG*', 'vector_Vec6f', 'vector_uchar', 'bool', 'double*', 'vector_vector_Point2f', 'float', 'Point2f', 'MatShape', 'vector_double', 'size_t', 'LayerId', 'vector_Vec4f', 'Net', 'vector_float', 'char', 'vector_int', 'Point2f*', 'vector_KeyPoint', 'vector_MatShape', 'RotatedRect', 'int*', 'Size', 'KeyPoint', 'vector_vector_Mat', 'Scalar', 'Point*', 'vector_Point', 'Mat', 'int', 'Ptr_float', 'vector_String', 'Rect', 'Point']

# print(decl[0])
# print(decl[1])
# print(decl[2])
# print(decl[3])
# parser.print_decls(decls)
print(len(decls))
print("namespaces:", " ".join(sorted(parser.namespaces)))

print("\n".join(list(set(argtypes))))
print("")
print("\n".join(list(set(defvals))))
