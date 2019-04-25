class TreeNode
  attr_accessor :val, :left, :right

  def initialize val, left=nil, right=nil
    @val = val
    @left = left
    @right = right
  end
end


def right_side_view root
  result = []
  level = 0
  q = [[root, 1]]

  while !q.empty?
    node, curr_level = q.shift
    
    if node
      if curr_level > level
        result << node.val
        level += 1
      end
      
      q << [node.right, level + 1]
      q << [node.left, level + 1]
    end
  end
  
  result
end


root = TreeNode.new(
  1,
  TreeNode.new(
    2,
    TreeNode.new(4),
    TreeNode.new(5)
  ),
  TreeNode.new(3, nil, TreeNode.new(6))
)

p right_side_view root
