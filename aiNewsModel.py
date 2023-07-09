from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
import torch

#  Load Model and Tokenize

tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/kobart-news")
model = BartForConditionalGeneration.from_pretrained("ainize/kobart-news")
# model = BartForConditionalGeneration.from_pretrained('/kobart_summary')
# tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')


# Generate Summary Text Ids

def generate_summary(input_text):
  input_ids = tokenizer.encode(input_text, return_tensors="pt")
  summary_text_ids = model.generate(
      input_ids=input_ids,
      bos_token_id=model.config.bos_token_id,
      eos_token_id=model.config.eos_token_id,
      length_penalty=2.0,
      max_length=128,
      min_length=32,
      num_beams=4,
  )
  output = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)

  return output



# def generate_summary(text):
#   input_ids = tokenizer.encode(text)
#   input_ids = torch.tensor(input_ids)
#   input_ids = input_ids.unsqueeze(0)

#   output = model.generate(input_ids, eos_token_id=1, max_length=512, min_length = 64, num_beams=5, length_penalty = 2.0)
#   output = tokenizer.decode(output[0], skip_special_tokens=True)
  
#   return output