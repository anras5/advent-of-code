package helpers

import "fmt"

type Stack[T any] struct {
	list []T
}

func NewStack[T any]() Stack[T] {
	return Stack[T]{}
}

func (stack *Stack[T]) Peek() T {
	if stack.Empty() {
		panic("Stack is empty")
	}
	return stack.list[len(stack.list)-1]
}

func (stack *Stack[T]) Push(elm T) {
	stack.list = append(stack.list, elm)
}

func (stack *Stack[T]) Pop() (elm T) {
	elm, stack.list = stack.Peek(), stack.list[0:len(stack.list)-1]
	return elm
}

func (stack *Stack[T]) Empty() bool {
	return len(stack.list) == 0
}

func (stack *Stack[T]) Reverse() {
	for i, j := 0, len(stack.list)-1; i < j; i, j = i+1, j-1 {
		stack.list[i], stack.list[j] = stack.list[j], stack.list[i]
	}
}

func (stack *Stack[T]) Print() {
	for _, v := range stack.list {
		fmt.Println(v)
	}
}
