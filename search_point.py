import pandas as pd
import numpy as np
import gradio as gr
import pickle
from sklearn.ensemble import IsolationForest

# Load the model
filename = "iforest.sav"
loaded_model = loaded_model = pickle.load(open(filename, 'rb'))
data = [[0,0,0]]
columns = ["duration_","src_bytes","dst_bytes"]
loaded_model.predict(pd.DataFrame(data, columns=columns))

# Return the answer in the GUI
def greet(duration, source_bytes, destination_bytes):
    data = [[duration,source_bytes,destination_bytes]]
    columns = ["duration_","src_bytes","dst_bytes"]
    # print(pd.DataFrame(data, columns=columns))
    ans = loaded_model.predict(pd.DataFrame(data, columns=columns))
    print(ans)
    return f'Given point is {"not" if ans==1 else ""} anomaly'
# Activate
if __name__ == '__main__':
    demo = gr.Interface(fn=greet, inputs=["number", "number", "number"], outputs="text")
    demo.launch(server_port=80,server_name='0.0.0.0')

