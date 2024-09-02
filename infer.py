# pip install onnxruntime
# wget https://github.com/thewh1teagle/nakdimon-ort/releases/download/v0.1.0/nakdimon.onnx

import onnxruntime as ort
import numpy as np

input = np.array([1, 2], dtype=np.float32)
input = input.reshape(1, -1)
session = ort.InferenceSession('nakdimon.onnx')
outputs = session.run(None, {'input_1': input})
print(outputs)