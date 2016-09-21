
def decode_cpsr(cpsr, leading_tabs=0):
    ret_str = ""
    armflag_N  = (cpsr >> 31) &  1
    armflag_Z  = (cpsr >> 30) &  1
    armflag_C  = (cpsr >> 29) &  1
    armflag_V  = (cpsr >> 28) &  1
    armflag_Q  = (cpsr >> 27) &  1
    armflag_J  = (cpsr >> 24) &  1
    armflag_GE = (cpsr >> 16) &  7
    armflag_E  = (cpsr >>  9) &  1
    armflag_A  = (cpsr >>  8) &  1
    armflag_I  = (cpsr >>  7) &  1
    armflag_F  = (cpsr >>  6) &  1
    armflag_T  = (cpsr >>  5) &  1
    armflag_M  = (cpsr >>  0) & 31


    ret_str += "\t"*leading_tabs + "        +----+----+----+----+----+----+----+----+\n"
    ret_str += "\t"*leading_tabs + "Legend: |NZCV|Q--J|----|GEGE|----|--EA|IFTM|MMMM|\n"
    ret_str += "\t"*leading_tabs + "        +----+----+----+----+----+----+----+----+\n"
    ret_str += "\t"*leading_tabs + "        |  x%X|  x%X|  x%X|  x%X|  x%X|  x%X|  x%X|  x%X|\n" % ( (cpsr & 0xf0000000) >> 28,
                                                                             (cpsr & 0x0f000000) >> 24,
                                                                             (cpsr & 0x00f00000) >> 20,
                                                                             (cpsr & 0x000f0000) >> 16,
                                                                             (cpsr & 0x0000f000) >> 12,
                                                                             (cpsr & 0x00000f00) >>  8,
                                                                             (cpsr & 0x000000f0) >>  4,
                                                                             (cpsr & 0x0000000f) >>  0)


    ret_str += "\t"*leading_tabs + "Actual: |"
    ret_str += "N" if armflag_N else " "
    ret_str += "Z" if armflag_Z else " "
    ret_str += "C" if armflag_C else " "
    ret_str += "V" if armflag_V else " "
    ret_str += "|"
    ret_str += "Q" if armflag_Q else " "
    ret_str += "--"
    ret_str += "J" if armflag_J else " "
    ret_str += "|"
    ret_str += "----"
    ret_str += "|"
    ret_str += "%d"% (armflag_GE & 8)
    ret_str += "%d"% (armflag_GE & 4)
    ret_str += "%d"% (armflag_GE & 2)
    ret_str += "%d"% (armflag_GE & 1)
    ret_str += "|"
    ret_str += "----"
    ret_str += "|"
    ret_str += "--"
    ret_str += "E" if armflag_E else " "
    ret_str += "A" if armflag_A else " "
    ret_str += "|"
    ret_str += "I" if armflag_I else " "
    ret_str += "F" if armflag_F else " "
    ret_str += "T" if armflag_T else " "
    ret_str += "%d" %( 1 if (armflag_M & 16) else 0)
    ret_str += "|"
    ret_str += "%d" %( 1 if (armflag_M & 8) else 0)
    ret_str += "%d" %( 1 if (armflag_M & 4) else 0)
    ret_str += "%d" %( 1 if (armflag_M & 2) else 0)
    ret_str += "%d" %( 1 if (armflag_M & 1) else 0)
    ret_str += "|"
    ret_str += "\n"
    ret_str += "\t"*leading_tabs + "        +----+----+----+----+----+----+----+----+\n"

    return ret_str

if __name__ == "__main__":
    import sys
    cpsr = int(sys.argv[1],16)
    print decode_cpsr(cpsr)
