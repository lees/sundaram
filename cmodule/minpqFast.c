#include <Python.h>

#define N 10000

struct keyvalue
{
    PyObject * key;
    PyObject * value;
};

int len;
struct keyvalue mas[N];


int less_sav(int i,int j)
{
    return PyObject_RichCompareBool(mas[i].key,mas[j].key,Py_LT);
}

#define less(i,j) PyObject_RichCompareBool(mas[i].key,mas[j].key,Py_LT)

void exchange(int i,int j)
{
    PyObject * temp_key;
    PyObject * temp_value;

    temp_key = mas[j].key;
    temp_value = mas[j].value;

    mas[j].key = mas[i].key;
    mas[j].value = mas[i].value;

    mas[i].key = temp_key;
    mas[i].value = temp_value;

}

void exchange_sav(int i,int j)
{
    struct keyvalue tmp;

    tmp = mas[j];
    mas[i] = tmp;

}


void swim(int k)
{
    while (k>1 && !less(k/2,k))
    {
        exchange(k/2,k);
        k /= 2;
    }
}

void sink(int k)
{
    int j = 2*k;

    while (j<=len)
    {
        if (j<len && !less(j,j+1))
        {
            j++;
        };
        if (!less(j,k))
        {
            break;
        };
        exchange(k,j);
        k = j;
        j *= 2;
    }
}




PyObject * insert( PyObject * self, PyObject * args)
{
    PyObject * key;
    PyObject * value;

    if (!PyArg_ParseTuple(args, "OO", &key,&value))
        return NULL;

    len++;

    mas[len].key = key;
    Py_INCREF(key);
    mas[len].value = value;
    Py_INCREF(value);
    swim(len);

    return Py_BuildValue("O", value);
}

PyObject * get(PyObject * self, PyObject * args)
{

    if (!len)
        return Py_BuildValue("i",0);

    exchange(1,len);

    len--;

    sink(1);

    return Py_BuildValue("O", mas[len+1].value);

}

 
PyObject * show(PyObject * self, PyObject * args)
{
    
   
    int i;   
    if (!PyArg_ParseTuple(args, "i", &i))
        return NULL;

    return Py_BuildValue("O",mas[i].value);

}

PyObject * length(PyObject * self, PyObject * args)
{
    return Py_BuildValue("i",len);
}

static PyMethodDef my_methods[] = 
{
    { "insert", (PyCFunction) insert, METH_VARARGS, "Insert the value into storage" },
    { "get", (PyCFunction) get, METH_VARARGS, "Get the value from storage" },
    { "show", (PyCFunction) show, METH_VARARGS, "show values in inner mas. debuging function" },
    { "length", (PyCFunction) length, METH_VARARGS, "show values in inner mas. debuging function" },
    { NULL, 0, 0, NULL }
};
 
void initminpqFast()
{
    len = 0;
    

    PyObject * module;
    module = Py_InitModule("minpqFast", my_methods);
    if (PyErr_Occurred())
        PyErr_SetString(PyExc_ImportError, "minpqFast module init failed");
}