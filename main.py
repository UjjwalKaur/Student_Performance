# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pickle

pickle_file_path = 'model.pkl'

try:
    with open(pickle_file_path, 'rb') as pickle_in:
        model = pickle.load(pickle_in)
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error("The specified pickle file was not found.")
except pickle.UnpicklingError:
    st.error("Error occurred while unpickling the file.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")


def predict_student_performance(hours, scores, extracurricular, sleep, question_papers):
    hours = int(hours)
    scores = int(scores)
    extracurricular = int(extracurricular)
    sleep = int(sleep)
    question_papers =  int(question_papers)
    prediction = model.predict([[hours, scores, extracurricular, sleep, question_papers]])
    return prediction


def main():
    st.title("Student Performance Prediction")
    hours_studied = st.text_input("Hours Studied", "Type Here")
    prev_scores = st.text_input("Previous Scores", "Type Here")
    extracurricular = st.text_input("Extracurricular Activities", "Type Here")
    sleep_hours = st.text_input("Sleep Hours", "Type Here")
    practised_question_papers = st.text_input("Sample Question Papers Practised", "Type Here")
    result = ""
    if st.button('Predict'):
        result = predict_student_performance(
            hours_studied, prev_scores, extracurricular, sleep_hours, practised_question_papers
        )
    st.success('Your predicted score is {}'.format(result))
    if st.button('About'):
        st.text('Built with streamlit')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#run the app and tell me what you see
#now, we have to add the inputs (add the inputs and let me know what you see on the terminal and on the app
#where is the input() function taking the input?
#this is because we have separate syntax for streamlit applications (it's only a little different)
#st.text_input()
#st.title()
#try to experiment a little bit if you can
#st.button('name of the button')
#if st.button(): will return either a True or a False
#st.write("string to be printed")
