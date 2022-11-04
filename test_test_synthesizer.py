from components.test_synthesizer.component import TestSynthesizer
from components.test_synthesizer.completion_prompt import CompletionPrompt


if __name__ == "__main__":

    prompt = CompletionPrompt(
        specification="print hello world",
        program_old="def hello():\n    print('hell')",
        program_new="def hello():\n    print('hello')",
        template_file="template.py",
    )
    synthesizer = TestSynthesizer("code-davinci-002", max_completion_tokens=500, stream=False)
    test = synthesizer.synthesize(prompt, temperature=0.0)