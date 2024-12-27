import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("My First Streamlit App")

    # Add a sidebar
    st.sidebar.header("Settings")
    
    # Create a selectbox in the sidebar
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line", "Bar", "Scatter"])

    # Generate some random data
    data = pd.DataFrame({
        'x': range(1, 11),
        'y': np.random.randn(10)
    })

    # Display the data
    st.subheader("Data")
    st.dataframe(data)

    # Create a chart based on user selection
    st.subheader("Chart")
    fig, ax = plt.subplots()

    if chart_type == "Line":
        ax.plot(data['x'], data['y'])
    elif chart_type == "Bar":
        ax.bar(data['x'], data['y'])
    else:  # Scatter
        ax.scatter(data['x'], data['y'])

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    st.pyplot(fig)

    # Add a text input and display the result
    user_input = st.text_input("Enter some text")
    if user_input:
        st.write(f"You entered: {user_input}")

    # Add a slider and display the result
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

if __name__ == "__main__":
    main()
