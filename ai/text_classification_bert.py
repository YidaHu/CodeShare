#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   text_classification_bert.py
@Time    :   2023/06/16 00:39:24
@Author  :   Yida Hu
@Version :   1.0
@Desc    :   None
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchtext.data import Field, TabularDataset, BucketIterator
from transformers import RobertaModel, RobertaTokenizer

# 定义RoBERTa模型
class RoBERTaModel(nn.Module):
    def __init__(self, output_dim):
        super(RoBERTaModel, self).__init__()
        self.roberta = RobertaModel.from_pretrained('roberta-base')
        self.fc = nn.Linear(self.roberta.config.hidden_size, output_dim)
        
    def forward(self, x):
        _, pooled_output = self.roberta(x)
        output = self.fc(pooled_output)
        return output

# 训练函数
def train(model, iterator, optimizer, criterion, device):
    model.train()
    
    for batch in iterator:
        optimizer.zero_grad()
        input_ids = batch.text.to(device)
        attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.long).to(device)
        predictions = model(input_ids, attention_mask=attention_mask)
        loss = criterion(predictions, batch.label.to(device))
        loss.backward()
        optimizer.step()

# 评估函数
def evaluate(model, iterator, criterion, device):
    model.eval()
    correct = 0
    total = 0
    loss = 0
    
    with torch.no_grad():
        for batch in iterator:
            input_ids = batch.text.to(device)
            attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.long).to(device)
            predictions = model(input_ids, attention_mask=attention_mask)
            loss = criterion(predictions, batch.label.to(device))
            loss += loss.item() * input_ids.size(0)
            _, predicted_labels = torch.max(predictions, dim=1)
            correct += (predicted_labels == batch.label.to(device)).sum().item()
            total += batch.label.size(0)
    
    accuracy = correct / total
    return loss / total, accuracy

if __name__ == "__main__":
    # 超参数
    batch_size = 32
    num_epochs = 10
    learning_rate = 1e-5
    output_dim = 2
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 加载预训练的RoBERTa模型和分词器
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RoBERTaModel(output_dim).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # 定义数据字段和数据集
    text_field = Field(tokenize=tokenizer.encode, use_vocab=False, pad_token=tokenizer.pad_token_id, batch_first=True)
    label_field = Field(sequential=False, use_vocab=False)
    fields = [('text', text_field), ('label', label_field)]
    train_data, test_data = TabularDataset.splits(
        path='./data', train='train.csv', test='test.csv', format='csv', fields=fields, skip_header=True
    )

    # 构建词汇表并初始化迭代器
    text_field.build_vocab(train_data, min_freq=2)
    train_iterator, test_iterator = BucketIterator.splits(
        (train_data, test_data), batch_size=batch_size, sort_key=lambda x: len(x

    # 训练模型
    for epoch in range(num_epochs):
        train(model, train_iterator, optimizer, criterion, device)
        train_loss, train_acc = evaluate(model, train_iterator, criterion, device)
        test_loss, test_acc = evaluate(model, test_iterator, criterion, device)
        print(f'Epoch: {epoch+1}/{num_epochs}, Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, Test Loss: {test_loss:.4f}, Test Acc: {test_acc:.4f}')

    # 保存模型
    torch.save(model.state_dict(), 'roberta_model.pth')

    # 示例推理
    example_text = "This is a positive sentence."
    encoded_text = tokenizer.encode(example_text, add_special_tokens=True)
    input_ids = torch.tensor(encoded_text).unsqueeze(0).to(device)
    attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.long).to(device)
    with torch.no_grad():
        model.eval()
        predictions = model(input_ids, attention_mask=attention_mask)
        _, predicted_labels = torch.max(predictions, dim=1)
        predicted_class = predicted_labels.item()
        print(f'Example Text: {example_text}')
        print(f'Predicted Class: {predicted_class}')