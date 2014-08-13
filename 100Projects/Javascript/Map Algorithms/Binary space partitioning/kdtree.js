function node(x, y, data) {
  this.point = [x, y];
  this.data = data;
  this.left = null;
  this.right = null;
}

function kDTree(points, n) {
  this.root = null;
  var i = 0;
  for (i=0; i<n; i++) {
    if (this.root) {
      var cur = this.root;
      j = 0;
      while (cur) {
        if (cur.point[j%2] > points[i][j%2]) {
          if (cur.left) {
            cur = cur.left;
          } else {
            cur.left = new node(points[i][0], points[i][1], points[i][2]);
            break;
          }
        } else {
          if (cur.right) {
            cur = cur.right;
          } else {
            cur.right = new node(points[i][0], points[i][1], points[i][2]);
            break;
          }
        }

        j++;
      }
    } else {
      this.root = new node(points[i][0], points[i][1], points[i][2]);
    }
  }
}