PROMPT_1 = """<|im_start|>system
Bạn là một trợ lí AI hữu ích. Hãy trả lời người dùng một cách chính xác.
<|im_end|>
<|im_start|>user
{}<|im_end|>
<|im_start|>assistant"""

PROMPT_2 = """[INST] <<SYS>>
Bạn là một trợ lí AI hữu ích. Hãy trả lời người dùng một cách chính xác.
<</SYS>>

{} [/INST]"""


pair_instruction = """Hãy xác định loại khía cạnh và trạng thái ý kiến (tốt, tạm, tệ) cho bình luận sau đây: \"{}\"\nTrả lời:"""

triplet_instruction = """Hãy xác định loại khía cạnh, cụm từ thể hiện khía cạnh và trạng thái ý kiến (tốt, tạm, tệ) cho bình luận sau đây: \"{}\"\nTrả lời:"""

quadruplet_instruction = """Hãy xác định loại khía cạnh, cụm từ thể hiện khía cạnh, cụm từ thể hiện ý kiến và trạng thái ý kiến (tốt tạm, tệ) cho bình luận sau đây: \"{}\"\nTrả lời:"""

def get_prompt(input_review, prompt_format, task):
    if task == 'pair':
        if prompt_format == '1':
            prompt = PROMPT_1.format(pair_instruction.format(input_review))
        elif prompt_format == '2':
            prompt = PROMPT_2.format(pair_instruction.format(input_review))
        else:
            prompt = pair_instruction.format(input_review)
    elif task == 'triplet':
        if prompt_format == '1':
            prompt = PROMPT_1.format(triplet_instruction.format(input_review))
        elif prompt_format == '2':
            prompt = PROMPT_2.format(triplet_instruction.format(input_review))
        else:
            prompt = triplet_instruction.format(input_review)
    elif task == 'quadruplet':
        if prompt_format == '1':
            prompt = PROMPT_1.format(quadruplet_instruction.format(input_review))
        elif prompt_format == '2':
            prompt = PROMPT_2.format(quadruplet_instruction.format(input_review))
        else:
            prompt = quadruplet_instruction.format(input_review)
    return prompt