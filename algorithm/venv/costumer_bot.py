import openai
import os

#needs to save as os eviorment parameter
openai.api_key = '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'

#Simulate the JS form parameters
parms = { 'company':'cable company', 
         'problem':' fault that the converter does not turn on', 
         'Characteristics':'adult does not understand technology'}

#Functio that create the bot characteristics
def create_bot(company, problem, characteristics):
    initial_prompt = f"I would like to schedule a customer service call for a {company} with you.\n"\
                     f"I would appreciate it if during the call you would act like a customer who {problem} \n"\
                     f"and act like {characteristics} \n"
    return initial_prompt

#Function that recives the Agent queries
def prompt_input():
    nlp_text = input("Enter your text:")
    return nlp_text


#Function that genetate the conversation each time and returns the answer of the costumers from the chatGPT
def coverstation_gen(parms, conv_until_now):
    conv_to_send = create_bot(parms['company'],parms['problem'],parms['Characteristics'])
    nlp_txt = prompt_input()
    while(nlp_txt != 'have a good day'):
        conv_to_send = conv_to_send + "Agent:" + nlp_txt
        query = conv_to_send + " \n please continue this coverstion and give only the Costumer next response"
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt= query,
            temperature = 0.7,
            max_tokens = 256,
            top_p = 1.0,
            frequency_penalty =0,
            presence_penalty = 0,
            stop= 'have a good day' #sentence to end session
            )
        print(response["choices"][0]["text"])
        conv_to_send = conv_to_send + response["choices"][0]["text"] + "\n "
        nlp_txt = prompt_input()
        

        
#testing -->
coverstation_gen(parms, "")

        
