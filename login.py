import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "mysql+mysqlconnector://root:hammad@localhost/sms_db"

# Setting up the database
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the Feedback model
class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    overall_service = Column(String(20))
    professionalism = Column(String(20))
    communication = Column(String(20))
    response_time = Column(String(20))
    appropriate_response = Column(String(20))
    safety = Column(String(20))
    safety_improvement = Column(String(20))
    interactions = Column(String(20))
    interaction_nature = Column(Text)
    trust = Column(String(20))
    confidence = Column(String(20))
    mistreatment = Column(String(20))
    mistreatment_details = Column(Text)
    improvements = Column(Text)
    additional_comments = Column(Text)
    age_group = Column(String(20))
    gender = Column(String(20))
    area_of_residence = Column(String(100))

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

def save_feedback(email, overall_service, professionalism, communication, response_time,
                   appropriate_response, safety, safety_improvement, interactions, interaction_nature,
                   trust, confidence, mistreatment, mistreatment_details, improvements,
                   additional_comments, age_group, gender, area_of_residence):
    new_feedback = Feedback(
        email=email,
        overall_service=overall_service,
        professionalism=professionalism,
        communication=communication,
        response_time=response_time,
        appropriate_response=appropriate_response,
        safety=safety,
        safety_improvement=safety_improvement,
        interactions=interactions,
        interaction_nature=interaction_nature,
        trust=trust,
        confidence=confidence,
        mistreatment=mistreatment,
        mistreatment_details=mistreatment_details,
        improvements=improvements,
        additional_comments=additional_comments,
        age_group=age_group,
        gender=gender,
        area_of_residence=area_of_residence
    )
    session.add(new_feedback)
    session.commit()

def main():
    st.title("Police Service Feedback Form")

    # Email input
    email = st.text_input("Email", "")

    if not email:
        st.error("Email is required")
        return

    # 1. Service Quality
    st.header("Service Quality")
    overall_service = st.radio("How would you rate the overall service provided by the police?",
                               ['Excellent', 'Good', 'Fair', 'Poor'])
    professionalism = st.radio("How satisfied were you with the professionalism and courtesy of the officers?",
                               ['Very Satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very Unsatisfied'])
    communication = st.radio("How clear and understandable was the communication from the police?",
                             ['Very Clear', 'Clear', 'Neutral', 'Unclear', 'Very Unclear'])

    # 2. Response Time
    st.header("Response Time")
    response_time = st.radio("How would you rate the police's response time to your incident?",
                             ['Excellent', 'Good', 'Fair', 'Poor'])
    appropriate_response = st.radio("Was the response time appropriate for the nature of the incident?",
                                    ['Yes', 'No', 'Unsure'])

    # 3. Safety and Security
    st.header("Safety and Security")
    safety = st.radio("How safe do you feel in your community?",
                      ['Very Safe', 'Safe', 'Neutral', 'Unsafe', 'Very Unsafe'])
    safety_improvement = st.radio("Have you noticed any improvement in safety in your community in the last year?",
                                  ['Yes', 'No', 'Unsure'])

    # 4. Interaction with Police
    st.header("Interaction with Police")
    interactions = st.radio("Have you had any interactions with the police in the last 6 months?",
                            ['Yes', 'No'])
    interaction_nature = st.text_area("If yes, please describe the nature of your interaction:") if interactions == 'Yes' else ""

    # 5. Trust and Confidence
    st.header("Trust and Confidence")
    trust = st.radio("How much do you trust the police to handle incidents in your community?",
                     ['Fully Trust', 'Somewhat Trust', 'Neutral', 'Distrust', 'Fully Distrust'])
    confidence = st.radio("Do you feel confident that the police will protect your rights and safety?",
                          ['Yes', 'No', 'Unsure'])

    # 6. Specific Incidents or Concerns
    st.header("Specific Incidents or Concerns")
    mistreatment = st.radio("Have you ever felt mistreated or unfairly treated by the police?",
                            ['Yes', 'No'])
    mistreatment_details = st.text_area("If yes, please explain:") if mistreatment == 'Yes' else ""
    improvements = st.text_area("What improvements would you like to see in police services:")

    # 7. Additional Comments
    st.header("Additional Comments")
    additional_comments = st.text_area("Please provide any additional comments or suggestions:")

    # 8. Demographics (Optional)
    st.header("Demographics (Optional)")
    age_group = st.radio("Age group:",
                         ['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'])
    gender = st.radio("Gender:",
                      ['Male', 'Female', 'Other', 'Prefer not to say'])
    area_of_residence = st.text_input("Area of residence:")

    if st.button("Submit"):
        save_feedback(email, overall_service, professionalism, communication, response_time,
                       appropriate_response, safety, safety_improvement, interactions, interaction_nature,
                       trust, confidence, mistreatment, mistreatment_details, improvements,
                       additional_comments, age_group, gender, area_of_residence)
        st.success("Thank you for your feedback!")

if __name__ == '__main__':
    main()
