# Audio
num_mels = 80
# num_freq = 1024
n_fft = 1024
sr = 22050
# frame_length_ms = 50.
# frame_shift_ms = 12.5
preemphasis = 0.98
frame_shift = null # seconds
frame_length = null # seconds
hop_length = 256# samples.
win_length = 1024 # samples.
n_mels = 80 # Number of Mel banks to generate
power = 1.5 # Exponent for amplifying the predicted magnitude
min_level_db = -100
ref_level_db = 20
hidden_size = 256
embedding_size = 512
max_db = 100
ref_db = 20
    
n_iter = 60
# power = 1.5
outputs_per_step = 1

epochs = 10000
lr = 0.001
save_step = 2000
image_step = 500
batch_size = 32

cleaners='english_cleaners'

data_path = '/data1/wangjiaqi/datasets/Haitian-031/'
checkpoint_path = '/data1/liuzhuangzhuang/transformer/checkpoint'
sample_path = '/data1/liuzhuangzhuang/transformer/samples'