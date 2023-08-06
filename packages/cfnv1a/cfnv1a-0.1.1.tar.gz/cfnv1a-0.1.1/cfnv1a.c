#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdint.h>


static PyObject* fnv1a(PyObject *self, PyObject *args, PyObject *kwds) {
    char* key;
    Py_ssize_t len;
    uint64_t prime = 1099511628211UL;
    uint64_t offset = 14695981039346656037UL;
    uint64_t result = offset;

    static char *kwlist[] = {"key", "prime", "offset", NULL};

    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "z#|ii", kwlist, &key, &len, &prime, &offset
    )) return NULL;

    for(int i=0; i<len; i++) {
        result = result ^ key[i];
        result = result * prime;
    }
    return PyLong_FromLong(result);
}


static PyMethodDef Cfnv1a_Methods[] = {
    {"fnv1a", fnv1a, METH_VARARGS | METH_KEYWORDS, "compute fvn1a hash"},
    {NULL, NULL, 0, NULL}
};


static PyModuleDef cfnv1a_module = {
    PyModuleDef_HEAD_INIT, "cfnv1a", "fnv1a c implementation for python",
    -1, Cfnv1a_Methods
};


PyMODINIT_FUNC PyInit_cfnv1a(void) {
    PyObject *m = PyModule_Create(&cfnv1a_module);
    if (m == NULL) return NULL;
    return m;
}
