class Program:
    def __init__(self, sections):
        self.sections = sections

    def accept(self, visitor):
        return visitor.visit_program(self)


class Section:
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions

    def accept(self, visitor):
        return visitor.visit_section(self)

class CnsI32Ins:
    def __init__(self, dest, lit_i32):
        self.dest = dest
        self.lit_i32 = lit_i32

    def accept(self, visitor):
        return visitor.visit_cns_i32_ins(self)


class AddIns:
    def __init__(self, dest, src0, src1):
        self.dest = dest
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_add_ins(self)


class SubIns:
    def __init__(self, dest, src0, src1):
        self.dest = dest
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_sub_ins(self)


class MulIns:
    def __init__(self, dest, src0, src1):
        self.dest = dest
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_mul_ins(self)


class DivIns:
    def __init__(self, dest, src0, src1):
        self.dest = dest
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_div_ins(self)


class ModIns:
    def __init__(self, dest, src0, src1):
        self.dest = dest
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_mod_ins(self)


class JumpIns:
    def __init__(self, at_location):
        self.at_location = at_location

    def accept(self, visitor):
        return visitor.visit_jump_ins(self)


class JeqIns:
    def __init__(self, at_location, src0, src1):
        self.at_location = at_location
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_jeq_ins(self)


class JltIns:
    def __init__(self, at_location, src0, src1):
        self.at_location = at_location
        self.src0 = src0
        self.src1 = src1

    def accept(self, visitor):
        return visitor.visit_jlt_ins(self)


class MoveIns:
    def __init__(self, dest, src0):
        self.dest = dest
        self.src0 = src0

    def accept(self, visitor):
        return visitor.visit_move_ins(self)


class PrintIns:
    def __init__(self, src0):
        self.src0 = src0

    def accept(self, visitor):
        return visitor.visit_print_ins(self)


class LitI32:
    def __init__(self, i32_tok):
        self.i32_tok = i32_tok

    def accept(self, visitor):
        return visitor.visit_lit_i32(self)


class Register:
    def __init__(self, reg_num: int):
        self.reg_num = reg_num

    def accept(self, visitor):
        return visitor.visit_register(self)


class Label:
    def __init__(self, lexeme: str):
        self.name = lexeme[:-1]

    def accept(self, visitor):
        return visitor.visit_label(self)


class AtLocation:
    def __init__(self, name):
        self.name = name
        self.address = None

    def accept(self, visitor):
        return visitor.visit_at_location(self)
