# This Python file uses the following encoding: utf-8
import mysql.connector
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


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

    def dataPetani(self):
        aksi = self.koneksi.cursor(dictionary = True)
        aksi.execute("select * from petani order by id_petani asc")
        return aksi.fetchall()

    def filterPetani(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute(
            "SELECT * FROM petani WHERE id_petani LIKE %s OR nama_petani LIKE %s OR alamat LIKE %s OR jenis_kelamin LIKE %s",
            ([f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"])
        )
        return aksi.fetchall()

    def cetakPetani(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM petani")
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Petani", "Nama", "Alamat", "No HP", "Jenis Kelamin", "Umur"]
        ] + list(data)

        fileLaporan = "Laporan Petani.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph("LAPORAN DATA PETANI", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 130, 160, 120, 130, 80])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)


    def cetakFilterPetani(self, jk):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM petani WHERE jenis_kelamin = %s", (jk,))
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Petani", "Nama", "Alamat", "No HP", "Jenis Kelamin", "Umur"]
        ] + list(data)

        fileLaporan = "Laporan Petani.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph(f"LAPORAN DATA PETANI ({jk})", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 130, 160, 120, 130, 80])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)



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

    def dataLahan(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                l.id_lahan,
                pt.nama_petani,
                l.lokasi,
                l.luas_lahan,
                l.jenis_tanah,
                l.keterangan
            FROM lahan l
            JOIN petani pt ON l.id_petani = pt.id_petani
            ORDER BY l.id_lahan ASC
        """)
        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def filterLahan(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                l.id_lahan,
                pt.nama_petani,
                l.lokasi,
                l.luas_lahan,
                l.jenis_tanah,
                l.keterangan
            FROM lahan l
            JOIN petani pt ON l.id_petani = pt.id_petani
            WHERE
                l.id_lahan LIKE %s OR
                pt.nama_petani LIKE %s OR
                l.lokasi LIKE %s OR
                l.jenis_tanah LIKE %s
            ORDER BY l.id_lahan ASC
        """, (f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"))

        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def cetakLahan(self):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                l.id_lahan,
                pt.nama_petani,
                l.lokasi,
                l.luas_lahan,
                l.jenis_tanah,
                l.keterangan
            FROM lahan l
            JOIN petani pt ON l.id_petani = pt.id_petani
        """)
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Lahan", "Nama Petani", "Lokasi", "Luas Lahan", "Jenis Tanah", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Lahan.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph("LAPORAN DATA LAHAN", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 140, 140, 100, 120, 180])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)

    def cetakFilterLahan(self, jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                l.id_lahan,
                pt.nama_petani,
                l.lokasi,
                l.luas_lahan,
                l.jenis_tanah,
                l.keterangan
            FROM lahan l
            JOIN petani pt ON l.id_petani = pt.id_petani
            WHERE l.jenis_tanah = %s
        """, (jenis,))

        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Lahan", "Nama Petani", "Lokasi", "Luas Lahan", "Jenis Tanah", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Lahan.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph(f"LAPORAN DATA LAHAN ({jenis})", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 140, 140, 100, 120, 180])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)


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

    def dataTanaman(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM tanaman ORDER BY id_tanaman ASC")
        return aksi.fetchall()

    def filterTanaman(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute(
            "SELECT * FROM tanaman WHERE id_tanaman LIKE %s OR nama_tanaman LIKE %s OR jenis_tanaman LIKE %s OR musim_tanam LIKE %s",
            ([f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"])
        )
        return aksi.fetchall()

    def cetakTanaman(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM tanaman")
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Tanaman", "Nama", "Jenis", "Masa Tanam", "Musim Tanam", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Tanaman.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph("LAPORAN DATA TANAMAN", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[70, 130, 120, 90, 110, 170])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)


    def cetakFilterTanaman(self, jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM tanaman WHERE jenis_tanaman = %s", (jenis,))
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Tanaman", "Nama", "Jenis", "Masa Tanam", "Musim Tanam", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Tanaman.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph(f"LAPORAN DATA TANAMAN ({jenis})", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[70, 130, 120, 90, 110, 170])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)



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
            "UPDATE pemupukan SET id_petani=%s, id_tanaman=%s, jenis_pupuk=%s, tanggal_pupuk=%s, jumlah_kg=%s, keterangan=%s WHERE id_pemupukan=%s ",
            (idpetani, idtanaman, jenis, tanggal, jumlah, ket, idpupuk))
        self.koneksi.commit()
        aksi.close()

    def hapusPemupukan(self, idpupuk):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM pemupukan WHERE id_pemupukan=%s", (idpupuk,))
        self.koneksi.commit()
        aksi.close()

    def dataPemupukan(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                p.id_pemupukan,
                pt.nama_petani,
                t.nama_tanaman,
                p.jenis_pupuk,
                p.tanggal_pupuk,
                p.jumlah_kg,
                p.keterangan
            FROM pemupukan p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            ORDER BY p.id_pemupukan ASC
        """)
        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def filterPemupukan(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                p.id_pemupukan,
                pt.nama_petani,
                t.nama_tanaman,
                p.jenis_pupuk,
                p.tanggal_pupuk,
                p.jumlah_kg,
                p.keterangan
            FROM pemupukan p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            WHERE
                p.id_pemupukan LIKE %s OR
                pt.nama_petani LIKE %s OR
                t.nama_tanaman LIKE %s OR
                p.jenis_pupuk LIKE %s
            ORDER BY p.id_pemupukan ASC
        """, (f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"))

        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def cetakPemupukan(self):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                p.id_pemupukan,
                pt.nama_petani,
                t.nama_tanaman,
                p.jenis_pupuk,
                p.tanggal_pupuk,
                p.jumlah_kg,
                p.keterangan
            FROM pemupukan p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
        """)
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID", "Petani", "Tanaman", "Jenis Pupuk", "Tanggal", "Jumlah (Kg)", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Pemupukan.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph("LAPORAN DATA PEMUPUKAN", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[70, 120, 120, 120, 100, 100, 150])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)

    def cetakFilterPemupukan(self, jenis):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                p.id_pemupukan,
                pt.nama_petani,
                t.nama_tanaman,
                p.jenis_pupuk,
                p.tanggal_pupuk,
                p.jumlah_kg,
                p.keterangan
            FROM pemupukan p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            WHERE p.jenis_pupuk = %s
        """, (jenis,))

        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID", "Petani", "Tanaman", "Jenis Pupuk", "Tanggal", "Jumlah (Kg)", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Pemupukan.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph(f"LAPORAN DATA PEMUPUKAN ({jenis})", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[70, 120, 120, 120, 100, 100, 150])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)


    # CRUD PANEN
    def tambahPanen(self, idpanen, idpetani, idtanaman, tanggal, jumlah, kualitas, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "INSERT INTO panen (id_panen, id_petani, id_tanaman, tanggal_panen, jumlah_hasil, kualitas, keterangan) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)", (idpanen, idpetani, idtanaman, tanggal, jumlah, kualitas, keterangan))
        self.koneksi.commit()
        aksi.close()

    def ubahPanen(self, idpanen, idpetani, idtanaman, tanggal, jumlah, kualitas, keterangan):
        aksi = self.koneksi.cursor()
        aksi.execute(
            "UPDATE panen SET id_petani=%s, id_tanaman=%s, tanggal_panen=%s, jumlah_hasil=%s, kualitas=%s, keterangan=%s WHERE id_panen=%s ",
            (idpetani, idtanaman, tanggal, jumlah, kualitas, keterangan, idpanen))
        self.koneksi.commit()
        aksi.close()

    def hapusPanen(self, idpanen):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM panen WHERE id_panen=%s", (idpanen,))
        self.koneksi.commit()
        aksi.close()

    def dataPanen(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                p.id_panen,
                pt.nama_petani,
                t.nama_tanaman,
                p.tanggal_panen,
                p.jumlah_hasil,
                p.kualitas,
                p.keterangan
            FROM panen p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            ORDER BY p.id_panen ASC
        """)
        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def filterPanen(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT
                p.id_panen,
                pt.nama_petani,
                t.nama_tanaman,
                p.tanggal_panen,
                p.jumlah_hasil,
                p.kualitas,
                p.keterangan
            FROM panen p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            WHERE
                p.id_panen LIKE %s OR
                pt.nama_petani LIKE %s OR
                t.nama_tanaman LIKE %s OR
                p.kualitas LIKE %s
            ORDER BY p.id_panen ASC
        """, (f"%{cari}%", f"%{cari}%", f"%{cari}%", f"%{cari}%"))

        hasil = aksi.fetchall()
        aksi.close()
        return hasil

    def cetakPanen(self):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                p.id_panen,
                pt.nama_petani,
                t.nama_tanaman,
                p.tanggal_panen,
                p.jumlah_hasil,
                p.kualitas,
                p.keterangan
            FROM panen p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
        """)
        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Panen", "Petani", "Tanaman", "Tanggal", "Jumlah Hasil", "Kualitas", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Panen.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph("LAPORAN DATA PANEN", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 130, 130, 100, 110, 100, 160])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)

    def cetakFilterPanen(self, kualitas):
        aksi = self.koneksi.cursor()
        aksi.execute("""
            SELECT
                p.id_panen,
                pt.nama_petani,
                t.nama_tanaman,
                p.tanggal_panen,
                p.jumlah_hasil,
                p.kualitas,
                p.keterangan
            FROM panen p
            JOIN petani pt ON p.id_petani = pt.id_petani
            JOIN tanaman t ON p.id_tanaman = t.id_tanaman
            WHERE p.kualitas = %s
        """, (kualitas,))

        data = aksi.fetchall()
        aksi.close()

        barisData = [
            ["ID Panen", "Petani", "Tanaman", "Tanggal", "Jumlah Hasil", "Kualitas", "Keterangan"]
        ] + list(data)

        fileLaporan = "Laporan Panen.pdf"

        pdf = SimpleDocTemplate(
            fileLaporan,
            pagesize=landscape(A4),
            leftMargin=60,
            rightMargin=60,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()
        elemen = []

        judul = Paragraph(f"LAPORAN DATA PANEN ({kualitas})", styles["Title"])
        elemen.append(judul)
        elemen.append(Spacer(1, 20))

        tabel = Table(barisData, colWidths=[80, 130, 130, 100, 110, 100, 160])

        tabel.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elemen.append(tabel)
        pdf.build(elemen)





