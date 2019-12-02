#  Karatek IceBearHole
#  Copyright (C) 2019  Karatek_HD
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sklearn import tree

# red, green, yellow, white [r, g, y, w]

features = [[5, 4, 6, 3], [4, 1, 5, 2], [4, 5, 5, 2], [5, 6, 3, 2], [6, 2, 2, 2], [1, 1, 4, 6], [5, 5, 1, 1],
            [2, 2, 6, 4], [1, 2, 6, 1], [2, 6, 4, 5], [4, 4, 6, 6], [1, 3, 3, 2], [2, 3, 5, 6], [2, 3, 4, 6],
            [1, 2, 4, 6], [1, 3, 4, 6], [1, 1, 5, 6], [2, 2, 3, 6], [3, 3, 5, 6], [2, 6, 3, 4], [6, 6, 5, 3],
            [2, 4, 4, 6], [1, 3, 3, 5], [2, 2, 4, 4], [4, 5, 5, 6], [1, 1, 5, 6], [2, 3, 4, 5], [4, 5, 6, 6]]
labels = [[2, 6], [2, 4], [2, 8], [2, 6], [0, 0], [2, 0], [4, 8],
          [0, 0], [2, 0], [1, 4], [0, 0], [2, 4], [2, 6], [1, 0],
          [1, 0], [2, 2], [3, 4], [1, 2], [3, 8], [1, 2], [2, 6],
          [0, 0], [4, 8], [0, 0], [2, 4], [4, 8], [2, 6], [1, 4]]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[3, 3, 4, 5]])
