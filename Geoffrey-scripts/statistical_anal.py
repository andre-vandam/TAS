import data_handler as dh

Dataset3 = dh.DataFrame('3.tas.csv')

Uxy_mag = dh.arr_vec_length (Dataset3.Uxy)

print(Uxy_mag)
