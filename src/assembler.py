import struct

from ast import *
from visitor import AbstractVisitor

bytecode = {
    "add": b"\x02",
    "sub": b"\x03",
    "mul": b"\x04",
    "div": b"\x05",
    "mod": b"\x06",
    "jump": b"\x13",
    "jeq": b"\x14",
    "jlt": b"\x15",
    "cns_i32": b"\x17",
    "move": b"\x1C",
    "print": b"\x1D",
}


class AssemblerError(Exception):
    def __init__(self, lineno, msg):
        self.lineno = lineno
        self.msg = msg


class AssemblerVisitor(AbstractVisitor):
    def assemble(self, node):
        return node.accept(self)

    def visit_program(self, program: Program):
        header = b"KLST"
        maj_ver = struct.pack("<H", 0)
        min_ver = struct.pack("<H", 3)

        byte_code = b"".join([self.assemble(section)
                              for section in program.sections])

        cns_size = struct.pack("<I", 0)
        ins_size = struct.pack("<I", len(byte_code))

        return header + maj_ver + min_ver + cns_size + ins_size + byte_code

    def visit_section(self, section: Section):
        return b"".join([self.assemble(statement) for statement in section.instructions])

    def visit_cns_i32_ins(self, i32_ins: CnsI32Ins):
        return bytecode["cns_i32"] + self.assemble(i32_ins.dest) + \
               self.assemble(i32_ins.lit_i32)

    def visit_add_ins(self, add_ins: AddIns):
        return bytecode["add"] + self.assemble(add_ins.dest) + \
               self.assemble(add_ins.src0) + \
               self.assemble(add_ins.src1)

    def visit_sub_ins(self, sub_ins: AddIns):
        return bytecode["sub"] + self.assemble(sub_ins.dest) + \
               self.assemble(sub_ins.src0) + \
               self.assemble(sub_ins.src1)

    def visit_mul_ins(self, mul_ins: AddIns):
        return bytecode["mul"] + self.assemble(mul_ins.dest) + \
               self.assemble(mul_ins.src0) + \
               self.assemble(mul_ins.src1)

    def visit_div_ins(self, div_ins: AddIns):
        return bytecode["div"] + self.assemble(div_ins.dest) + \
               self.assemble(div_ins.src0) + \
               self.assemble(div_ins.src1)

    def visit_mod_ins(self, mod_ins: ModIns):
        return bytecode["mod"] + self.assemble(mod_ins.dest) + \
               self.assemble(mod_ins.src0) + \
               self.assemble(mod_ins.src1)

    def visit_jump_ins(self, jump_ins: JumpIns):
        return bytecode["jump"] + self.assemble(jump_ins.at_location)

    def visit_jeq_ins(self, jeq_ins: JeqIns):
        return bytecode["jeq"] + self.assemble(jeq_ins.at_location) + \
               self.assemble(jeq_ins.src0) + \
               self.assemble(jeq_ins.src1)

    def visit_jlt_ins(self, jump_lt_ins: JltIns):
        return bytecode["jlt"] + self.assemble(jump_lt_ins.at_location) + \
               self.assemble(jump_lt_ins.src0) + \
               self.assemble(jump_lt_ins.src1)

    def visit_move_ins(self, move_ins: MoveIns):
        return bytecode["move"] + self.assemble(move_ins.dest) + \
               self.assemble(move_ins.src0)

    def visit_print_ins(self, print_ins: PrintIns):
        return bytecode["print"] + self.assemble(print_ins.src0)

    def visit_register(self, reg: Register):
        return struct.pack("<B", reg.reg_num)

    def visit_lit_i32(self, lit_i32: LitI32):
        return struct.pack("<I", int(lit_i32.i32_tok.lexeme))

    def visit_label(self, label: Label):
        return b""

    def visit_at_location(self, at_location: AtLocation):
        return struct.pack("<b", at_location.address)
