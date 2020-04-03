
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

interface TabBar {
  props: IProps;
  state: PageState
}
@connect(({ counter }) => ({
  counter
}), (dispatch) => ({

}))
class TabBar extends Component {
  static config: Config = {
    navigationBarTitleText: 'TabBar'
  }
  static options: ComponentOptions = {
    "addGlobalClass": true
  }
  state = {

  }
  componentDidMount() {
    
  }
  render() {
    const { } = this.state;
    const { } = this.props.counter;
    return (
      <View>
      TabBar
      </View >
    )
  }
}
export default TabBar as ComponentClass<PageOwnProps, PageState>

