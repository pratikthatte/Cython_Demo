# Cython Demo

This GitHub repository contains the Cython demo code for my **MATH 608** project.

## Prerequisites
Before running the code, ensure that the Cython compiler is installed on your machine.

## Steps to Follow

1. **Build the Extension Module**
   - For **macOS/Linux** users:  
     ```bash
     python setup.py build_ext --inplace -i
     ```
   - For **Windows** users:  
     ```bash
     python setup.py build_ext --inplace -i --compiler=mingw32 -DMS_WIN64
     ```

2. **Test the Runtime Performance**  
   Run the script to test the runtimes using the following command:  
   ```bash
   python test_runtime.py

