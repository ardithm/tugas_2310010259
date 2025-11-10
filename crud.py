# This Python file uses the following encoding: utf-8
import mysql.connector

class crud_tugas:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'db_2310010259')


    # CRUD PETANI
    def tambahPetani(self, id, nm, alamat, no, jk, umur):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into petani (id_petani, nama_petani, alamat, no_hp, jenis_kelamin, umur) value(%s, %s, %s, %s, %s, %s)",
        (id, nm, alamat, no, jk, umur))
        self.koneksi.commit()
        aksi.close()

    def ubahPetani(self, id, nm, alamat, no, jk, umur):
        aksi = self.koneksi.cursor()
        aksi.execute("update petani set nama_petani = %s, alamat = %s, no_hp = %s, jenis_kelamin = %s, umur = %s where id_petani = %s",
        (nm, alamat, no, jk, umur, id))
        self.koneksi.commit()
        aksi.close()

    def hapusPetani (self, id):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from petani where id_petani = %s",
        (id, ))
        self.koneksi.commit()
        aksi.close()

    #CRUD LAHAN
    def tambahLahan(self, idlahan, idpetani, lokasi, luas, jenis, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute("insert into lahan (id_lahan, id_petani, lokasi, luas_lahan, jenis_tanah, keterangan) value(%s, %s, %s, %s, %s, %s)",
        (idlahan, idpetani, lokasi, luas, jenis, keterangan))
        self.koneksi.commit()
        aksi.close()

    def ubahLahan(self, idlahan, idpetani, lokasi, luas, jenis, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute("update lahan set id_petani = %s, lokasi = %s, luas_lahan = %s, jenis_tanah = %s, keterangan = %s where id_lahan = %s",
        (idpetani, lokasi, luas, jenis, keterangan, idlahan))
        self.koneksi.commit()
        aksi.close()

    def hapusLahan(self, idlahan):
        aksi = self.koneksi.cursor()
        aksi.execute("delete from lahan where id_lahan = %s",
        (idlahan, ))
        self.koneksi.commit()
        aksi.close()

    def tampilPetani(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT id_petani, nama_petani FROM petani")
        hasil = aksi.fetchall()
        aksi.close()
        return hasil


    # CRUD TANAMAN
    def tambahTanaman(self, idtanaman, nama, jenis, masa, musim, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO tanaman (id_tanaman, nama_tanaman, jenis_tanaman, masa_tanam, musim_tanam, keterangan) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (idtanaman, nama, jenis, masa, musim, keterangan)
        )
        self.koneksi.commit()
        aksi.close()

    def ubahTanaman(self, idtanaman, nama, jenis, masa, musim, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "UPDATE tanaman SET nama_tanaman=%s, jenis_tanaman=%s, masa_tanam=%s, musim_tanam=%s, keterangan=%s "
            "WHERE id_tanaman=%s",
            (nama, jenis, masa, musim, keterangan, idtanaman)
        )
        self.koneksi.commit()
        aksi.close()

    def hapusTanaman(self, idtanaman):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM tanaman WHERE id_tanaman=%s", (idtanaman,))
        self.koneksi.commit()
        aksi.close()

    # CRUD PEMUPUKAN
    def tambahPemupukan(self, idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO pemupukan (id_pemupukan, id_petani, id_tanaman, jenis_pupuk, tanggal_pupuk, jumlah_kg, keterangan) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)", (idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket))
        self.koneksi.commit()
        aksi.close()

    def ubahPemupukan(self, idpupuk, idpetani, idtanaman, jenis, tanggal, jumlah, ket):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "UPDATE pemupukan SET id_petani=%s, id_tanaman=%s, jenis_pupuk=%s, tanggal_pupuk=%s, jumlah_kg=%s, keterangan=%s WHERE id_pemupukan=%s "
            (idpetani, idtanaman, jenis, tanggal, jumlah, ket, idpupuk))
        self.koneksi.commit()
        aksi.close()

    def hapusPemupukan(self, idpupuk):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM pemupukan WHERE id_pemupukan=%s", (idpupuk,))
        self.koneksi.commit()
        aksi.close()

    def tampilPemupukan(self):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT p.id_pemupukan, pt.nama_petani, t.nama_tanaman, p.jenis_pupuk, p.tanggal_pupuk, p.jumlah_kg, p.keterangan
            FROM pemupukan p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            """)
        hasil = aksi.fetchall()
        aksi.close()
        return hasil





