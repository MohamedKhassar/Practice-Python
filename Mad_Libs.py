def main():
    prompt={
        "adjective": "",
        "noun": "",
        "verb": "",
        "place": "",
        "plural_noun": ""
    }
    
    for pr in prompt:
        while not prompt[pr]:
            answer=get_input(f"Enter a {pr}: ")
            prompt[pr]=answer

    story=f"One day, a {prompt["adjective"]} {prompt["noun"]} decided to {prompt["verb"]} through the {prompt["place"]}. Along the way, it found a {prompt["adjective"]} {prompt["noun"]} and they became best {prompt["plural_noun"]}."
    print(story)

def get_input(placeholder):
    answer=input(placeholder)
    return answer

main()