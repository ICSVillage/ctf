from pycomm3 import Struct, DINT, UINT, Revision, n_bytes, UDINT, SHORT_STRING

whoStruct = Struct(
    UINT("vendor"),
    UINT("product_type"),
    UINT("product_code"),
    Revision("revision"),
    n_bytes(2, "status"),
    UDINT("serial"),
    SHORT_STRING("product_name"),
)
