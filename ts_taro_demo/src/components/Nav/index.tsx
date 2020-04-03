import Taro, { Component, Config, ComponentOptions } from '@tarojs/taro'
import { View } from '@tarojs/components'
import { ComponentClass } from 'react'
import './index.scss'
import { connect } from '@tarojs/redux'

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

interface Nav {
  props: IProps;
  state: PageState
}
@connect(({ counter }) => ({
  counter
}), (dispatch) => ({

}))
class Nav extends Component {
  static config: Config = {
    navigationBarTitleText: 'Demo'
  }
  static options: ComponentOptions = {
    "addGlobalClass": true
  }
  componentDidMount() {
    console.log(this)
  }
  state = {
  }
  render() {
    const { } = this.state;
    const { } = this.props.counter;
    return (
      <View>
        Top
      </View >
    )
  }
}
export default Nav as ComponentClass<PageOwnProps, PageState>
