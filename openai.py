import openai as ai
import paramiko
import time
import speech_recognition as sr
 

ai.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def generate_gpt3_response(user_text, print_output=False):
    completions = ai.Completion.create(
        engine='text-davinci-003',  
        temperature=0.5,            
        prompt=user_text,           
        max_tokens=100,             
        n=1,                        
        stop=None,                  
    )

    if print_output:
        print(completions)

    return completions.choices[0].text

def push_config(config):
	user = 'hugo'
	password = 'hugo'
	port=22
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect('192.168.223.138',port, user, password, look_for_keys=False)
	chan = ssh.invoke_shell()
	time.sleep(2)
	chan.send('conf t\n')
	chan.send(config + '\n')
	time.sleep(5)
	output = chan.recv(999999)
	print(output.decode("utf-8"))


r = sr.Recognizer()
with sr.Microphone() as source:
    global text
    r.adjust_for_ambient_noise (source, duration = 1)
    print("What's UP HUGO")
    audio = r.listen(source, timeout=100, phrase_time_limit=100)
    print("Recognizing...")
    try:
    	text = r.recognize_google(audio,language="en-ENG")
    	print(text)
    except Exception as e:
        print("Error: " + str(e))


prompt = str(text)


response = generate_gpt3_response(prompt)
print(response)
config=str(response)
push_config(config)
