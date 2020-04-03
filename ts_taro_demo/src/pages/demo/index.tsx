import Taro, { Component, Config } from '@tarojs/taro'
import { View } from '@tarojs/components'
import { ComponentClass } from 'react'
import './index.scss'
import { connect } from '@tarojs/redux'
import Nav from '@/components/Nav'
import { test } from '@api'
type PageStateProps = {
  counter: any
}
type PageDispatchProps = {
}
type PageOwnProps = {
}
type PageState = {
}
type IProps = PageStateProps & PageDispatchProps & PageOwnProps

interface Brand {
  props: IProps;
  state: PageState
}
@connect(({ counter }) => ({
  counter
}), (dispatch) => ({

}))
class Brand extends Component {
  config: Config = {
    navigationBarTitleText: 'Demo'
  }
  state = {
  }
  componentDidMount() {
    console.log(this)
    test().then((res: any) => {
      console.log(res)
    })
  }
  render() {
    const { } = this.state;
    const { } = this.props.counter;
    return (
      <View>
        <View className="main">Body</View>
        <Nav />
      </View >
    )
  }
}
export default Brand as ComponentClass<PageOwnProps, PageState>
