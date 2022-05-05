import pandas as pd 
import streamlit as st 

st.write('**Tính tiền nhà trọ **')

# Số điện
dc = int(st.number_input('Số điện cũ:',0,99999))
dm = int(st.number_input('Số điện mới:',dc,99999))
# Số nước
st.write('--------')
nc = int(st.number_input('Số nước cũ:',0,99999))
nm = int(st.number_input('Số nước mới',nc,99999))
# Net
st.write('--------')
net = int(st.number_input('Net',0, 120,step=40))
# Nhà
st.write('--------')
nha = int(st.number_input('Nha trọ',500, 2000,step=100))
# Đơn giá
dd = 6
dn = 20

# Tạo dataframe để hiện kết quả
df = pd.DataFrame(columns = ['Điện', 'Nước'], index=['Số mới', 'Số cũ', 'Chênh lệch', 'Đơn giá', 'Thành tiền','Tạm tính', 'Net', 'Nhà', 'Tổng'])
df.loc['Số mới', 'Điện']=dm
df.loc['Số cũ', 'Điện']=dc
df.loc['Số mới', 'Nước']=nm
df.loc['Số cũ', 'Nước']=nc
df.loc['Chênh lệch','Điện']=dm-dc
df.loc['Chênh lệch','Nước']=nm-nc
df.loc['Đơn giá','Điện']=dd
df.loc['Đơn giá','Nước']=dn
t_dien = dd*(dm-dc)
t_nuoc = dn*(nm-nc)
t_tinh = t_dien+t_nuoc
df.loc['Thành tiền','Điện']=t_dien
df.loc['Thành tiền','Nước']=t_nuoc
df.loc['Tạm tính','Điện']=t_tinh
df.loc['Net','Điện']=net
df.loc['Nhà','Điện']=nha
df.loc['Tổng','Điện']=t_tinh+net+nha
df=df.fillna(value=0)


st.dataframe(df)