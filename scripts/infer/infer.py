# import sys
# import os
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# if project_root not in sys.path:
#     sys.path.append(project_root)

from lumina_mgpt.inference_solver import FlexARInferenceSolver
from PIL import Image

# ******************** Image Generation ********************
inference_solver = FlexARInferenceSolver(
    model_path="Alpha-VLLM/Lumina-mGPT-7B-768",
    precision="bf16",
    target_size=768,
)

q1 = f"Generate an image of 768x768 according to the following prompt:\n \
     Image of a dog playing water, and a waterfall is in the background."

# generated: tuple of (generated response, list of generated images)
temperature=0
import torch
import time
decoding_time = time.time()
with torch.no_grad():
    generated = inference_solver.generate(
        images=[],
        qas=[[q1, None]],
        max_gen_len=8192,
        temperature=temperature,
        logits_processor=inference_solver.create_logits_processor(cfg=4.0, image_top_k=2000),
    )
decoding_time = time.time()-decoding_time

a1, new_image = generated[0], generated[1][0]
print(a1, new_image)
file_path = f"/home/leihaodong/ICCV25/lumina-mGPT/output_image_T{temperature}.png"
new_image.save(file_path)  # 保存为 PNG 格式
print("图像已保存为 output_image.png")
print(decoding_time)
# print(a1.shape, new_image.shape)
exit()
# # ******************* Image Understanding ******************
# inference_solver = FlexARInferenceSolver(
#     model_path="Alpha-VLLM/Lumina-mGPT-7B-512",
#     precision="bf16",
#     target_size=512,
# )

# # "<|image|>" symbol will be replaced with sequence of image tokens before fed to LLM
# q1 = "Describe the image in detail. <|image|>"

# images = [Image.open("image.png")]
# qas = [[q1, None]]

# # `len(images)` should be equal to the number of appearance of "<|image|>" in qas
# generated = inference_solver.generate(
#     images=images,
#     qas=qas,
#     max_gen_len=8192,
#     temperature=1.0,
#     logits_processor=inference_solver.create_logits_processor(cfg=4.0, image_top_k=2000),
# )

# a1 = generated[0]
# # generated[1], namely the list of newly generated images, should typically be empty in this case.


# # ********************* Omni-Potent *********************
# inference_solver = FlexARInferenceSolver(
#     model_path="Alpha-VLLM/Lumina-mGPT-7B-768-Omni",
#     precision="bf16",
#     target_size=768,
# )

# # Example: Depth Estimation
# # For more instructions, see demos/demo_image2image.py
# q1 = "Depth estimation. <|image|>"
# images = [Image.open("image.png")]
# qas = [[q1, None]]

# generated = inference_solver.generate(
#     images=images,
#     qas=qas,
#     max_gen_len=8192,
#     temperature=1.0,
#     logits_processor=inference_solver.create_logits_processor(cfg=1.0, image_top_k=200),
# )

# a1 = generated[0]
# new_image = generated[1][0]
