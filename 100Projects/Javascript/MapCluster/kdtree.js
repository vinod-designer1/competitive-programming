function Node(x, y, data) {
  this.x = x;
  this.y = y;
  this.data = data;
  this.left = null;
  this.right = null;
}

function insert(x, y, ktree, cid) {
  if (cid === 0) {
    if (ktree.x > x) {
      if (ktree.left) {
        insert(x, y, ktree.left, (cid+1)%2);
      } else {
        ktree.left = Node(x, y);
      }
    } else if (ktree.x < x) {
      if (ktree.right) {
        insert(x, y, ktree.right, (cid+1)%2);
      } else {
        ktree.right = Node(x, y);
      }
    }
  } else {
    if (ktree.y > y) {
      if (ktree.left) {
        insert(x, y, ktree.left, (cid+1)%2);
      } else {
        ktree.left = Node(x, y);
      }
    } else if (ktree.y < y) {
      if (ktree.right) {
        insert(x, y, ktree.right, (cid+1)%2);
      } else {
        ktree.right = Node(x, y);
      }
    }
  }
}


function findMin(ktree, dim, cid) {
  var leftMin,
      rightMin;

  if (ktree) {
   if (cd === dim) {
     if (ktree.left) {
       findMin(ktree.left, dim, (cid+1)%2);
     } else {
       return ktree.data;
     }
   } else {
     return Math.min(
       findMin(ktree.left, dim, (cid+1)%2),
       findMin(ktree.right, dim, (cid+1)%2),
       ktree.data
     );
   }
  }

  return null;
}

function deleteNode(point, ktree, cd) {
  var nextCd = (cd+1)%2;
  if (ktree) {
    if (ktree.data === point) {
      if (ktree.right) {
        ktree.data = findMin(ktree.right, cd, nextCd);
        ktree.right = deleteNode(ktree.data, ktree.right, nextCd);
      } else if (ktree.left) {
        ktree.data = findMin(ktree.left, cd, nextCd);
        ktree.right = deleteNode(ktree.data, ktree.left, nextCd);
      } else {
        ktree = null;
      }
    }
  }

  return null;
}