
# Q: How to find out all states in the US whose name starts with a vowel?

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
		  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
		  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
		  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
		  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
		  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
		  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
		  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


# method 1
vowel_states = []
for state in states:
	if state[:1] in 'AEIOU':
		vowel_states.append(state)
print(f'Method 1 results: {vowel_states}.\n\n')

# method 2
vowel_states = [state for state in states if state[:1] in 'AEIOU']
print(f'Method 2 results: {vowel_states}.\n\n')


# Q: the word length of each state
state_len = {state: len(state) for state in states}
print(f'The word length of each state: {state_len}\n\n')


# Q: what happend when we run the `[]` line or `{}` line?
# - the expression is evaluated
# - the iteration is happened
#
# Q: what if we are trying to iterate the whole Wikipedia?
# - we definitely cannot afford loading everything into the memory
# - we have to evluate on demand

state_iterator = (state for state in states)
print(f'State iterator does not print anything: {state_iterator}')
