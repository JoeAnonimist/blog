# The QAbstractTableModel class provides an abstract 
# model that can be subclassed to create table models.

import sys
from PyQt6.QtWidgets import (QApplication, 
    QWidget, QHBoxLayout, QTableView)
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        database = QSqlDatabase('QSQLITE')
        database.setDatabaseName('chinook.db')
        database.open()

        genres_model = QSqlTableModel(db=database)
        genres_model.setTable('genres')
        genres_model.select()
        
        self.genres_view = QTableView()
        self.tracks_view = QTableView()
        
        self.genres_view.setModel(genres_model)
        self.genres_view.clicked.connect(self.show_tracks)
        
        layout.addWidget(self.genres_view)
        layout.addWidget(self.tracks_view)
        
    def show_tracks(self):
        
        current_index = self.genres_view.currentIndex()
        row = current_index.row()
        record = self.genres_view.model().record(row)
        
        genre_id = record.field('GenreId').value()
        
        database = self.genres_view.model().database()
        tracks_model = QSqlTableModel(db=database)
        tracks_model.setTable('tracks')
        tracks_model.setFilter('GenreId = {}'.format(genre_id))
        tracks_model.select()
        
        self.tracks_view.setModel(tracks_model)


if __name__ == '__main__':

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
