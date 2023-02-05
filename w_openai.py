import openai, yaml 
# I want to turn this into a object etc.
# WIP 9/2/23
#============================================================================================
def ProcessYAML (yaml_file) :
    """This function opens the yaml file and returns the data objec

    Args:
        yaml_file (file): yaml file to be loaded

    Returns:
        (boolean, object): returns debug flag and the yaml object
    """
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (debug, y_data)  

#=============================================================================================================    

if __name__ == "__main__":                          #only run when this is called by itself and not imported
    # Apply for an API key on the OpenAI website, then set it as follows:
    debug, yaml_data = ProcessYAML('settings.yaml')  
    openai.api_key = yaml_data['api_key']

    # Generate text using the OpenAI GPT-3 model
    model_engine = "text-davinci-002"
    #prompt = "What is the capital of France?"
    #prompt = "Write a nice short WhatsApp message that I can send to my wife."
    #prompt = "Tell me something about this exact day in history."
    #prompt = "What day is today?"
    #prompt = "Write a tweet with an inspirational quote in it."
    #prompt = "Write a short tweet for https://twitter.com/wvdsteen"
    prompt = "Say something that makes me want to click"
    responses = 1

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=responses,
        stop=None,
        temperature=0.5,

    )
    #message = completions.choices[0].text
    #print(message)
    print(len(completions.choices))
   
    for m in completions.choices :
        print(m.text)


    