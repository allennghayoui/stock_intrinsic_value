import streamlit as st
import requests
import json

from secret import call_api



def get_comapany_data(symbol):
    api_url = call_api(symbol)
    response = requests.get(api_url)
    return json.loads(response.text)[0]


def user_interface():
    st.title("Intrinsic Value Finder")
    with st.form("Search"):
        symbol = st.text_input("Symbol", key="symbol")

        submitted = st.form_submit_button("Get Value")

        if submitted:
            st.title("Value")
            value = get_comapany_data(symbol.upper())

            if value:
                st.write(f"Symbol: {value['symbol']}")
                st.write(f"Date: {value['date']}")
                st.write(f"Current Stock Price: {value['Stock Price']}")
                st.write(f"Intrinsic Value(DCF): {value['dcf']}")


def main():
    user_interface()
        

if __name__ == '__main__':
    main()
