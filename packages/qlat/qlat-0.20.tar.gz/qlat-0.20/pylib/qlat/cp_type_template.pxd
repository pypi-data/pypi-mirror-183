cdef class ElemTypeTYPENAME(ElemType):

    pass

cdef class FieldTYPENAME(FieldBase):

    cdef cqlat.Field[cqlat.TYPENAME] xx

    cdef readonly long cdata
